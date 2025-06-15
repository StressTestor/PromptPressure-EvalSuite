# PromptPressure Eval Suite — Version 1.5.0  
*2025-06-12*

## Added
- **LM Studio adapter** (`adapters/lmstudio_adapter.py`) for local LLMs.
- **Dataset validator** (`scripts/validate_dataset.py`) with duplicate-check and CI-friendly exit codes.
- **Progress bar** (`tqdm`) integration in `run_eval.py`.
- **Timestamped output filenames** to prevent accidental overwrites.
- **Runtime `register()` helper** for adding custom adapters on the fly.

## Fixed
- Runner now uses the single canonical `evals_dataset.json`; removed all references to the old v1.2 file.
- Schema validation catches missing keys and duplicate prompts before runs.

## Changed
- Adapter constant renamed to `ADAPTER_REGISTRY`.
- Default output naming pattern: `eval_scores_{provider}_{model}_{YYYYMMDD-HHMM}.csv`.
- README quick-start and example configs updated for v1.5 paths.

## Notes
- v1.5 finalises the 1.x “plumbing” series.  All core files are stable for the upcoming v2.0 dashboard & plugin work.
