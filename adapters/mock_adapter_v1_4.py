"""
PromptPressure Mock Adapter v1.4

Returns a mock response for simulation/testing.
"""

def generate_response(prompt, model_name="mock", config=None):
    """
    Return a mock, simulated response for eval logic.
    Args:
        prompt (str): User prompt.
        model_name (str): Model name (ignored).
        config (dict): Optional configuration (ignored).
    Returns:
        str: Simulated/mock response.
    """
    return f"[SIMULATED v1.4 RESPONSE] {prompt[::-1]}"
