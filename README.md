# PromptPressure Eval Suite v1.4

A high-quality evaluation suite to assess large language models (LLMs) for refusal mapping, instruction following, tone consistency, and emergent reasoning—now with **modular adapter architecture** for easy extension to any API or local model.

---

## Project Overview

- **Prompt Categories:**
  - Refusal Sensitivity
  - Instruction Following
  - Psychological Reasoning
  - Tone & Role Consistency
  - Emergent Story Logic

- **Modular Adapters (v1.4+):**
  - Easily add or swap model backends (Groq, OpenAI, Mock, etc.).
  - Adapter files live in `/adapters/` and expose a single `generate_response()` interface.

- **Key Files:**
  - `run_eval.py` — CLI runner (plug-in adapter logic)
  - `adapters/` — Model interface files (Groq, OpenAI, Mock, etc.)
  - `config.yaml` — Configures model, dataset, and options (YAML)
  - `evals_dataset.json` — Test suite with behavioral criteria
  - `eval_scores_output_*.csv` — Evaluation results (all outputs normalized)
  - `CHANGELOG_v1.4.md` — Detailed list of new features and changes

---

## Quickstart

**1. Clone the repo and install dependencies:**
```sh
git clone https://github.com/YourUsername/PromptPressure-EvalSuite.git
cd PromptPressure-EvalSuite
pip install -r requirements.txt
2. Create a .env file in your project root with your API keys:

env
Copy
Edit
GROQ_API_KEY=your-groq-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
3. (Optional but recommended) Save .gitignore in your repo root:

gitignore
Copy
Edit
.env
__pycache__/
*.pyc
.vscode/
.idea/
*.csv
.DS_Store
(See full recommended .gitignore in this README.)

Usage
List available adapters:

sh
Copy
Edit
python run_eval.py --list-adapters
Run an evaluation:

sh
Copy
Edit
python run_eval.py --model groq --config config.yaml --output eval_scores_output_groq.csv
Supported models (out-of-the-box):

groq (LLama3 via Groq API)

openai (OpenAI GPT models)

mock (simulation/testing only)

Config options:
Configure config.yaml or pass as CLI arguments:

model (groq/openai/mock)

model_name (e.g., llama3-70b-8192)

dataset (path to your JSON prompt set)

is_simulation (True/False)

Environment Variables
Place your API keys in a .env file in your project root:

env
Copy
Edit
GROQ_API_KEY=your-groq-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
Do not commit your .env file to GitHub!

Adapters
Adapters are in /adapters/:

groq_adapter_v1_4.py

openai_adapter_v1_4.py

mock_adapter_v1_4.py

Add your own by implementing a generate_response(prompt, model_name, config) function and adding it to ADAPTER_REGISTRY_V1_4 in adapters/__init__.py.

Output
Results are written to CSV (optionally JSON in future versions), with columns:

prompt_id

category

model_provider

model_name

input

response

refusal

format_compliance

response_time_sec

is_simulation

.gitignore Example
Place this at your repo root to keep secrets and junk out of Git:

gitignore
Copy
Edit
# Python, env, and system files
.env
.env.*
*.env
__pycache__/
*.pyc
*.pyo
*.pdm.toml
.vscode/
.idea/
*.csv
.DS_Store
Thumbs.db
requirements.txt
A minimal requirements.txt for your project:

nginx
Copy
Edit
pandas
requests
pyyaml
python-dotenv
Install with:

sh
Copy
Edit
pip install -r requirements.txt
Changelog
See CHANGELOG_v1.4.md for all updates.

License
MIT License. Fork, extend, and contribute!

Credits
Project by Joeseph Grey for OpenAI’s API Research & Evals initiative.
Adapter system and modular evals powered by user feedback and OpenAI best practices.