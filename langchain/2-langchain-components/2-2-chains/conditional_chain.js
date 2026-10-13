import { RunnableBranch, RunnableLambda } from "@langchain/core/runnables";

const analyzeFeedback = (text) => ({
    feedback: text,
    sentiment: text.toLowerCase().includes("love") ? "good" : "bad",
});

const goodBranch = new RunnableLambda(
    (data) => `Thank you for your feedback: ${data.feedback}`
);
const badBranch = new RunnableLambda(
    (data) => `Email support about: ${data.feedback}`
);

const feedbackChain = new RunnableLambda(analyzeFeedback).pipe(
    RunnableBranch.from([
        [(data) => data.sentiment === "good", goodBranch],
        badBranch,
    ])
);

console.log(await feedbackChain.invoke("I love this product!"));
console.log(await feedbackChain.invoke("The app keeps crashing."));

// output:
// Thank you for your feedback: I love this product!
// Email support about: The app keeps crashing.