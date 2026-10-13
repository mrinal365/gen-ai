from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Summarize {topic} in {emotion} tone"
)

print(prompt.format(topic="Cricket", emotion="fun"))

# output: Summarize Cricket in fun tone 
