# PromptPressure Eval Suite v1.5

A high-quality evaluation harness for large-language models (LLMs)—mapping
refusals, instruction-following, tone stability, and emergent reasoning.
Now with *local-model* support and a built-in dataset validator.

---

## ✨ What’s New in v1.5
- **LM Studio adapter** (`adapters/lmstudio_adapter.py`) for fully-local LLMs.
- **Schema validator** (`scripts/validate_dataset.py`) catches bad or
  duplicate prompts before a run—ideal for CI.
- **Single canonical dataset** `evals_dataset.json` (old v1.2 file removed).
- **Progress bar & timestamped outputs** in `run_eval.py`.
- Adapter hub renamed to `ADAPTER_REGISTRY` and exposed via `register()`.

---

## Project Layout
| Path | Purpose |
|------|---------|
| `run_eval.py` | CLI runner—pluggable adapter architecture |
| `adapters/` | Model interface files (Groq, OpenAI, LM Studio, Mock) |
| `scripts/validate_dataset.py` | JSON schema & duplicate checker |
| `config.yaml` / `config_lmstudio.yaml` | Example configs |
| `evals_dataset.json` | Prompt suite with eval criteria |
| `eval_scores_*.csv` | Results saved here (auto-timestamped) |
| `CHANGELOG_v1.5.md` | Full release notes |

---

## 🚀 Quick Start

1. **Clone & install deps**
   ```bash
   git clone https://github.com/YourUsername/PromptPressure-EvalSuite.git
   cd PromptPressure-EvalSuite
   pip install -r requirements.txt
Add API keys (if you’ll use cloud models) to .env

ini
Copy
Edit
GROQ_API_KEY=...
OPENAI_API_KEY=...
Validate the dataset (recommended)

bash
Copy
Edit
python scripts/validate_dataset.py evals_dataset.json
Run an evaluation

Groq (cloud):

bash
Copy
Edit
python run_eval.py --model groq --config config.yaml
LM Studio (local):

bash
Copy
Edit
python run_eval.py --model lmstudio \
                   --config config_lmstudio.yaml
🧩 Built-in Adapters
Key	Backend
groq	GroqCloud (Llama 3, Gemma, etc.)
openai	GPT family via OpenAI API
lmstudio	Local LLM served by LM Studio
mock	Deterministic stub for testing

Add your own adapter by implementing

python
Copy
Edit
def generate_response(prompt: str, model_name: str, config: dict) -> str
and registering it:

python
Copy
Edit
from adapters import register
register("myadapter", my_generate_fn)
📝 Output Schema (CSV)
Column	Description
prompt_id	Index of prompt in dataset
category	Prompt category (refusal, tone … )
model_provider / model_name	Where the response came from
input, response	Raw text
refusal	Boolean heuristic
format_compliance	Bullet/step check (nullable)
response_time_sec	Wall-clock latency
is_simulation	Marks synthetic runs

⚙️ Requirements
nginx
Copy
Edit
pandas
tqdm
pyyaml
python-dotenv
requests
Install via pip install -r requirements.txt.

🛠️ Contributing
Fork & branch off main.

Run scripts/validate_dataset.py and pytest before PRs.

Update CHANGELOG_v1.5.md for user-facing changes.

📄 License
MIT—fork, extend, and contribute.

Project by Joeseph Grey. Built with community feedback and OpenAI best
practices.

markdown
Copy
Edit
