import tiktoken

# Get the tokenizer encoding associated with GPT-4o
encoder = tiktoken.encoding_for_model("gpt-4o")

# Number of token IDs in this encoding's vocabulary
print("Vocabulary size:", encoder.n_vocab)

# Text to tokenize
text = "The cat sat on the mat"

# Convert text into a list of integer token IDs
tokens = encoder.encode(text)
print("Tokens:", tokens)

# Convert the token IDs back into readable text
decoded = encoder.decode(tokens)
print("Decoded:", decoded)

# Count tokens, useful for estimating input size
print("Token count:", len(tokens))


# prereq: pip install tiktoken
 