import dspy

MODEL_ID = "anthropic/claude-sonnet-4-5-20250929"
#API_BASE = "http://localhost:11434" # to test with local ollama: dspy.LM(MODEL_ID, api_base=API_BASE)
API_KEY = "THE_REAL_KEY"

def load_model():
    return dspy.LM(MODEL_ID, api_key=API_KEY)