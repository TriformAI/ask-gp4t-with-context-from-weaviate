import os
import json
from langchain_openai import (
    OpenAIEmbeddings,
)  # Facilitates using OpenAI's API for embeddings.
import weaviate  # Client library for interacting with Weaviate, a vector database.

# Retrieve Weaviate credentials and URL from environment variables.
WEAVIATE_API_KEY = os.environ["WEAVIATE_API_KEY"]
WEAVIATE_URL = os.environ["WEAVIATE_URL"]


def handler(event, context):
    # Extract the input text/question from the event payload.
    input = event.get("input_0")

    # Validate presence of input to ensure there's a question for processing.
    if not input:
        return {"error": "No question provided"}

    # Initialize the Weaviate client with API credentials for subsequent queries.
    client = weaviate.Client(
        url=WEAVIATE_URL, auth_client_secret=weaviate.AuthApiKey(WEAVIATE_API_KEY)
    )

    # Utilize OpenAIEmbeddings to generate a vector representation of the input text.
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    nearVector = {
        "vector": embeddings.embed_documents([input])[0]
    }  # Embed the input and unpack the first (only) element.

    # Perform a Weaviate query to find the top 4 closest "Article" vectors to the input vector.
    response = (
        client.query.get(
            "Article", ["text"]
        )  # Selects 'text' field from the matched 'Article' objects.
        .with_near_vector(
            nearVector
        )  # Filters objects by vector proximity to the input's vector.
        .with_limit(4)
        .do()  # Limits the response to the top 4 closest matches.
    )

    # Extracts 'text' from each article in the response, concatenating them with line breaks.
    texts = [article["text"] for article in response["data"]["Get"]["Article"]]
    combined_text = "\n".join(texts) + "\n"

    # Returns a JSON string with the concatenated texts and original question, formatted for readability.
    return json.dumps({"retrieved_context": combined_text, "question": input}, indent=2)
