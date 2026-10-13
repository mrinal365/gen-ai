import { ChatPromptTemplate } from "@langchain/core/prompts";

const chatPrompt = ChatPromptTemplate.fromMessages([
    ["system", "Hi, you are an experienced {profession}."],
    ["human", "Tell me about {topic}."],
]);

const formattedMessages = await chatPrompt.formatMessages({
    profession: "Doctor",
    topic: "Viral Fever",
});

console.log(formattedMessages);

// output:  [
//   SystemMessage(content="Hi, you are an experienced Doctor."),
//   HumanMessage(content="Tell me about Viral Fever.")
// ]