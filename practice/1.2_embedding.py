from openai import OpenAI
from dotenv import load_dotenv

# Load OPENAI_API_KEY from the .env file
load_dotenv()

# The SDK reads the API key from the environment
client = OpenAI()

text = (
    "Eiffel Tower is in Paris and is a famous landmark. "
    "It is 324 meters tall."
)

# Generate an embedding for the input text
response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

# Extract the numerical vector from the response
vector = response.data[0].embedding
print("Embedding:", vector)
print("Vector dimensions:", len(vector))