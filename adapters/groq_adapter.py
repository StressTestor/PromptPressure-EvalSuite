"""
PromptPressure Groq Adapter v1.4

Handles API calls to Groq for LLM completion.
"""

import os
import requests

def generate_response(prompt, model_name="llama3-70b-8192", config=None):
    """
    Generate a response from Groq LLM.
    Args:
        prompt (str): User prompt.
        model_name (str): Groq model name.
        config (dict): Optional configuration.
    Returns:
        str: Model-generated response.
    """
    api_key = os.getenv("GROQ_API_KEY") or (config.get("groq_api_key") if config else None)
    if not api_key:
        raise ValueError("Missing GROQ_API_KEY in environment or config.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": config.get("temperature", 0.7) if config else 0.7
    }
    endpoint = config.get("groq_endpoint", "https://api.groq.com/openai/v1/chat/completions") if config else "https://api.groq.com/openai/v1/chat/completions"
    response = requests.post(endpoint, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
