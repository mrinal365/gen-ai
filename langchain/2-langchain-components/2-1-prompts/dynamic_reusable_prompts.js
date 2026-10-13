import { PromptTemplate } from "@langchain/core/prompts";

const prompt = PromptTemplate.fromTemplate(
    "Summarize {topic} in {emotion} tone"
);

console.log(
    await prompt.format({ topic: "Cricket", emotion: "fun" })
);

// output: Summarize Cricket in fun tone 
