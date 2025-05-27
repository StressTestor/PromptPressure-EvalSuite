# PromptPressure Eval Suite v1.4 – 2025-05-27

## Added
- Modular adapter architecture: plug-and-play support for Groq, OpenAI, mock, and local adapters in `/adapters/`
- `run_eval.py` now dynamically loads adapters via `ADAPTER_REGISTRY_V1_4`
- CLI `--list-adapters` flag for instant discovery of available models
- Standardized output structure (`is_simulation`, `model_provider`, etc.) in every CSV row
- Example `.env` file for API key management, and documented `.env` usage in README
- Sample `.gitignore` and `requirements.txt` for clean, secure, and fast onboarding
- Robust config templates (`config.yaml`, `config_lmstudio.yaml`) for Groq, OpenAI, and local runs

## Fixed
- Consistent CSV output and error reporting across simulation and live runs
- Import and config logic cleaned for easier onboarding and reduced breakage
- Redundant/duplicate prompt datasets removed (now standardized on `evals_dataset.json`)
- Output filenames and config structure normalized for clarity

## Changed
- Project file structure clarified for adapters, config, and core scripts
- Documentation (`README.md`) now details `.env` security, config formats, and CLI usage
- Output and config naming conventions updated to match selected model/provider

## Security & Hygiene
- `.env` support for API secrets, with `.gitignore` recommendation to prevent accidental leaks
- Removed all API keys and secrets from tracked files
- Explicit onboarding comments in config files and docs

## Notes
- v1.4 is the final core logic and modularization milestone before 2.0 (dashboard, plugins, extensibility)
- Legacy scripts (`groq_batch_eval.py`) remain as-is for reference but should migrate to adapters in future
- Adapter registry enables rapid addition of new providers (local, cloud, or API)
- Batch and interactive scoring now leverage unified schema and fields

---

Release maintained by Joeseph Grey, with feedback from the OpenAI Evals community.  
All project files and onboarding materials reviewed for clarity and accuracy prior to public release.
