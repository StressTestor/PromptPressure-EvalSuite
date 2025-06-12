
"""LM Studio adapter for PromptPressure Eval Suite."""

import os
import requests

DEFAULT_ENDPOINT = "http://localhost:1234/v1/chat/completions"


def generate_response(prompt: str, model_name: str, config: dict | None = None) -> str:
    """Return the assistant message from an LM Studio /v1/chat/completions call.

    Args:
        prompt: User prompt (single‑turn).
        model_name: Model identifier as configured inside LM Studio.
        config: Optional dict with keys:
            - lmstudio_endpoint (str)
            - temperature (float)
            - max_tokens (int)

    Raises:
        requests.HTTPError: if the HTTP request fails.
        RuntimeError: if the response payload is malformed.
    """
    cfg = config or {}
    endpoint = cfg.get("lmstudio_endpoint", os.getenv("LMSTUDIO_ENDPOINT", DEFAULT_ENDPOINT))
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": cfg.get("temperature", 0.7),
    }
    if "max_tokens" in cfg:
        payload["max_tokens"] = cfg["max_tokens"]

    resp = requests.post(endpoint, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Malformed LM Studio response: {data}") from exc
