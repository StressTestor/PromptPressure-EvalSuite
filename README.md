# Prompt Pressure: An Evaluation Suite for Model Refusal, Tone, and Reasoning

This repository contains a high-quality evaluation suite built to assess large language models (LLMs) across nuanced use cases involving instruction following, refusal risk, psychological reasoning, and tone consistency.

Built as a candidate-led project inspired by OpenAI's call for "high quality evals" (Michelle Pokrass, AMA 2024), this suite is designed to test where models fall short in realistic, user-facing interactions.

---

## Project Overview

- **Prompt Categories:**
  - Refusal Sensitivity
  - Instruction Following
  - Psychological Reasoning
  - Tone & Role Consistency
  - Emergent Story Logic

- **Files Included:**
  - `evals_dataset.json`: JSON test suite of 50 prompts + scoring criteria
  - `eval_scores_output.csv`: Example scoring results (perfect scenario)
  - `eval_scores_interactive.csv`: Manual scoring loop output (simulated)
  - `eval_scores_batch.csv`: Model vs. model comparison (GPT-4, Hermes 3, etc.)

---

## Scoring System

Each test includes:
- A prompt (`input`)
- A set of evaluation criteria (`eval_criteria`)
- Expected behavior (`expected_behavior`)

Each model response is evaluated against these traits with a binary score (True/False), then totaled.

---

## Why This Matters

Many powerful LLMs struggle with nuanced requests that fall just outside hardcoded safety boundaries. This suite measures how models handle moral-safe edge cases, structured instructions, and character tone without over-refusing or derailing.

This project demonstrates:
- Real user pain points in model interaction
- Scalable and structured eval design
- Manual and automated scoring options

---

## Inspired By

> “New high quality evals are always impressive. I’m hiring for my team for user and product focused researchers with a love of evals!”  
> – *Michelle Pokrass, API Research Lead @ OpenAI*

---

## License

MIT License. Feel free to fork, extend, and build with it.

---

*Created by Joeseph Grey — remote-ready, eval-obsessed, and model-agnostic.*
