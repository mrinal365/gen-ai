from langchain_core.runnables import RunnableLambda, RunnableParallel

summarize = RunnableLambda(lambda text: f"Summary: {text[:35]}...")
sentiment = RunnableLambda(
    lambda text: "Positive" if "love" in text.lower() else "Neutral/Negative"
)

parallel_chain = RunnableParallel(
    summary=summarize,
    sentiment=sentiment,
)

result = parallel_chain.invoke("I love this app; it makes planning much easier.")
print(result)

# output
# {
#   'summary': 'Summary: I love this app; it makes planning...',
#   'sentiment': 'Positive'
# }