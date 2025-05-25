# PromptPressure Eval Suite v1.2

## Overview
PromptPressure is an LLM evaluation suite designed to stress-test refusal behavior, formatting logic, tone drift, and emergent narrative coherence.

Version 1.2 introduces formal simulation tracking and lays groundwork for recursion/loop behavior detection.

## What’s New in v1.2
- Added `is_simulation` flag to all scoring files (`output`, `batch`, `interactive`)
- Introduced loop detection scaffolding (v2-ready)
- Recompiled prompt suite and outputs from v1.1 base
- Full regeneration protocol: no partial updates allowed

## Core Files
- `evals_dataset_v1_2.json` – 20 structured prompts, unchanged from v1.1
- `eval_scores_output_v1_2.csv` – Primary results
- `eval_scores_batch_v1_2.csv` – Summary stats
- `eval_scores_interactive_v1_2.csv` – Human/manual scores
- `README.md`, `changelog.md` – Current version info

## Usage
This version supports mock simulation and real API runs (Groq, OpenAI, etc.). Scoring files now contain a `is_simulation` field for filtering simulation vs. execution.

