# Triform.ai Template: Text-Based Query Handler with Weaviate and OpenAI Embeddings

## Overview

This Python module integrates OpenAI's embedding capabilities with Weaviate's vector database to handle text-based queries efficiently. It is designed to help Triform.ai users easily initiate workflows involving semantic search or contextual retrieval from stored data.

## How it Works

The `handler` function takes an input text from an event payload, generates an embedding of the text using OpenAI's models, and queries a Weaviate database to find the most relevant texts based on vector similarity. The closest matching texts are then returned together with the original question, formatted as a JSON string.

## Use Cases

- Semantic search in knowledge bases to find relevant articles or documents.
- Enhancing customer support systems by retrieving contextually similar previous inquiries and solutions.
- Content recommendation systems where relevance and context play critical roles.

## Customization

- Modify the `model` parameter in `OpenAIEmbeddings` to use different models for embedding depending on the use case or desired accuracy.
- Change the query structure in Weaviate to adjust the number of retrieved documents or to modify the search criteria.
- Adapt the module to work with different vector databases by changing the `weaviate.Client` initialization and query methods.

## Environment Setup

Set the following environment variables:
- `WEAVIATE_API_KEY`: Your Weaviate instance's API key.
- `WEAVIATE_URL`: The URL endpoint for your Weaviate instance.