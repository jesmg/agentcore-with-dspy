import os
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from model.load import load_model
import dspy

app = BedrockAgentCoreApp(debug=True)
log = app.logger
lm = load_model()
dspy.configure(lm=lm)

# Define a simple function tool
def evaluate_math(expression: str):
    return dspy.PythonInterpreter({}).execute(expression)

@app.entrypoint
async def invoke(payload, context):

    # Create agent
    agent = dspy.ReAct(
        "question -> answer: float",
        tools=[evaluate_math]
    )

    pred = agent(question=payload.get("prompt"))
    return pred.answer

if __name__ == "__main__":
    app.run()