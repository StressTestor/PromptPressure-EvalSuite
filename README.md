# PromptPressure Eval Suite v1.3

## Overview
PromptPressure is an LLM evaluation suite designed to stress-test refusal behavior, formatting logic, tone drift, and emergent narrative coherence.

Version 1.3 introduces a full CLI-based runner, model-switching support, YAML config loading, and local API support for Groq and LM Studio.

---

## v1.3 Features
- ✅ CLI execution with `run_eval.py`
- ✅ Config-driven runs with `config.yaml` and `config_lmstudio.yaml`
- ✅ Supports Groq, LM Studio (localhost), and mock/simulated models
- ✅ Double-click launcher via `run_promptpressure_dynamic.bat`
- ✅ Auto-generates model-tagged output files (e.g. `eval_scores_output_llama3.csv`)
- ✅ Tracks `is_simulation`, response time, format compliance, and refusal detection

---

## File Summary

| File | Purpose |
|------|---------|
| `run_eval.py` | CLI runner with Groq + LM Studio support |
| `config.yaml` | Groq model test config |
| `config_lmstudio.yaml` | Local LM Studio config |
| `evals_dataset_v1_2.json` | Full 20-prompt test suite |
| `run_promptpressure_dynamic.bat` | Double-click launcher |
| `README.md` | This file |

---

## How to Run

#### 🧪 Groq:
Set your API key in `.env`, then run:
```bash
python run_eval.py --config config.yaml
```

#### 🧪 LM Studio:
Make sure LM Studio is running on `http://localhost:1234`, then:
```bash
python run_eval.py --config config_lmstudio.yaml
```

#### 🧪 Simulated Test:
```bash
python run_eval.py --model mock
```

---

## Output
Each run creates a uniquely named `.csv` such as:
```
eval_scores_output_llama3_70b_8192.csv
eval_scores_output_qwen3_8b.csv
```

These files track prompt ID, model name, provider, response, refusal status, format compliance, and response time.

---

## License
MIT — use freely, fork responsibly, contribute optionally.

---

Created by [Joeseph Grey](https://github.com/StressTestor)  
Version 1.3 — May 2025  
PromptPressure: Stress Testing AI on the Human Terms™
