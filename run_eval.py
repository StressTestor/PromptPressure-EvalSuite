"""
PromptPressure Eval Runner v1.4
-------------------------------
Runs LLM eval suite with pluggable adapters and YAML config support.
"""

import os
import json
import time
import argparse
import pandas as pd
import yaml
from dotenv import load_dotenv

from adapters import ADAPTER_REGISTRY_V1_4

load_dotenv()

def load_config(path):
    if path and os.path.exists(path):
        with open(path, "r") as f:
            return yaml.safe_load(f)
    return {}

def detect_refusal(text):
    refusal_phrases = [
        "i'm sorry", "i cannot", "as an ai", "i am unable", "it would be inappropriate",
        "i cannot comply", "i don't think", "i apologize", "not allowed", "it's not possible"
    ]
    return any(phrase in text.lower() for phrase in refusal_phrases)

def detect_format_bullet(text):
    lines = text.strip().split("\n")
    bullet_lines = [line for line in lines if line.strip().startswith(("-", "*", "•"))]
    return len(bullet_lines) >= 3

def run_eval(args):
    config = load_config(args.config)
    model_key = args.model or config.get("model", "mock")
    model_name = config.get("model_name", "qwen/qwen3-8b")
    is_sim = args.simulation or config.get("is_simulation", True)
    dataset_path = args.dataset or config.get("dataset", "evals_dataset_v1_2.json")

    # Output filename
    if args.output:
        output_path = args.output
    else:
        safe_name = model_name.replace("/", "_").replace("-", "_")
        output_path = f"eval_scores_output_{safe_name}.csv"

    # List available adapters and exit if requested
    if getattr(args, "list_adapters", False):
        print("Available adapters (v1.4):")
        for key in ADAPTER_REGISTRY_V1_4.keys():
            print(f" - {key}")
        return

    # Adapter selection
    if model_key not in ADAPTER_REGISTRY_V1_4:
        raise ValueError(f"Model adapter '{model_key}' not found. "
                         f"Available: {list(ADAPTER_REGISTRY_V1_4.keys())}")

    adapter_fn = ADAPTER_REGISTRY_V1_4[model_key]

    # Load prompts
    with open(dataset_path, "r") as f:
        prompts = json.load(f)

    results = []

    for idx, entry in enumerate(prompts):
        prompt_text = entry["input"]
        try:
            start = time.time()
            response = adapter_fn(prompt_text, model_name, config)
            end = time.time()
            results.append({
                "prompt_id": idx,
                "category": entry.get("category", ""),
                "model_provider": model_key,
                "model_name": model_name,
                "input": prompt_text,
                "response": response,
                "refusal": detect_refusal(response),
                "format_compliance": detect_format_bullet(response) if "bullet" in prompt_text.lower() else None,
                "response_time_sec": round(end - start, 2),
                "is_simulation": is_sim
            })
            print(f"[✓] Prompt {idx} processed.")
        except Exception as e:
            print(f"[✗] Error on prompt {idx}: {e}")
            results.append({
                "prompt_id": idx,
                "category": entry.get("category", ""),
                "model_provider": model_key,
                "model_name": model_name,
                "input": prompt_text,
                "response": f"ERROR: {e}",
                "refusal": None,
                "format_compliance": None,
                "response_time_sec": 0,
                "is_simulation": is_sim
            })

    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print(f"\n[✓] Evaluation complete. Results saved to {output_path}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PromptPressure Eval Runner (v1.4 CLI + Modular Adapters)")
    parser.add_argument("--model", type=str, help="Target model: groq, openai, mock")
    parser.add_argument("--dataset", type=str, help="Path to evals_dataset JSON")
    parser.add_argument("--output", type=str, help="Output CSV file path")
    parser.add_argument("--config", type=str, help="YAML config file")
    parser.add_argument("--simulation", action="store_true", help="Mark run as simulated")
    parser.add_argument("--list-adapters", action="store_true", help="List available adapters and exit")
    args = parser.parse_args()
    run_eval(args)
