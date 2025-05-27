"""
PromptPressure Adapters Init (v1.4)
-----------------------------------
Exposes model adapter registry for use in run_eval.py or batch runners.
"""

from .groq_adapter_v1_4 import generate_response as groq_generate_response
from .openai_adapter_v1_4 import generate_response as openai_generate_response
from .mock_adapter_v1_4 import generate_response as mock_generate_response

ADAPTER_REGISTRY_V1_4 = {
    "groq": groq_generate_response,
    "openai": openai_generate_response,
    "mock": mock_generate_response
}
