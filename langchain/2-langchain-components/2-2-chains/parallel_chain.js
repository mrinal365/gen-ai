import { RunnableLambda, RunnableParallel } from "@langchain/core/runnables";

const summarize = new RunnableLambda(
    (text) => `Summary: ${text.slice(0, 35)}...`
);
const sentiment = new RunnableLambda(
    (text) => text.toLowerCase().includes("love") ? "Positive" : "Neutral/Negative"
);

const parallelChain = new RunnableParallel({
    summary: summarize,
    sentiment,
});

console.log(
    await parallelChain.invoke("I love this app; it makes planning much easier.")
);


// output
// {
//   'summary': 'Summary: I love this app; it makes planning...',
//   'sentiment': 'Positive'
// }