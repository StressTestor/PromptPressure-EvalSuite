
"""Adapter registry for PromptPressure Eval Suite."""

from typing import Callable, Dict

__version__ = "1.5.0"

# Built‑in adapters
from .groq_adapter import generate_response as _groq_generate
from .openai_adapter import generate_response as _openai_generate
from .mock_adapter import generate_response as _mock_generate

try:
    from .lmstudio_adapter import generate_response as _lmstudio_generate  # type: ignore
except Exception:  # pragma: no cover
    def _lmstudio_generate(*_a, **_kw):  # type: ignore
        raise RuntimeError("lmstudio_adapter unavailable or misconfigured.")

ADAPTER_REGISTRY: Dict[str, Callable[..., str]] = {
    "groq": _groq_generate,
    "openai": _openai_generate,
    "mock": _mock_generate,
    "lmstudio": _lmstudio_generate,
}


def register(name: str, fn: Callable[..., str]) -> None:
    if name in ADAPTER_REGISTRY:
        raise KeyError(f"Adapter '{name}' already registered.")
    ADAPTER_REGISTRY[name] = fn
