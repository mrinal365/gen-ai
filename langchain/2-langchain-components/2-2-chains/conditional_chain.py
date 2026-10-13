from langchain_core.runnables import RunnableBranch, RunnableLambda

def analyze_feedback(text):
    return {"feedback": text, "sentiment": "good" if "love" in text.lower() else "bad"}

good_branch = RunnableLambda(
    lambda data: f"Thank you for your feedback: {data['feedback']}"
)
bad_branch = RunnableLambda(
    lambda data: f"Email support about: {data['feedback']}"
)

feedback_chain = RunnableLambda(analyze_feedback) | RunnableBranch(
    (lambda data: data["sentiment"] == "good", good_branch),
    bad_branch,  # Default route
)

print(feedback_chain.invoke("I love this product!"))
print(feedback_chain.invoke("The app keeps crashing."))

# output
# Thank you for your feedback: I love this product!
# Email support about: The app keeps crashing.