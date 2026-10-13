from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Hi, you are an experienced {profession}."),
    ("human", "Tell me about {topic}."),
])

formatted_messages = chat_prompt.format_messages(
    profession="Doctor",
    topic="Viral Fever",
)

print(formatted_messages)


# output:  [
#   SystemMessage(content="Hi, you are an experienced Doctor."),
#   HumanMessage(content="Tell me about Viral Fever.")
# ]