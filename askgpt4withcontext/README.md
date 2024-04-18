# Triform.ai Template: Contextual Chat Handler

## Overview

This Python module integrates with OpenAI's Chat models to provide context-driven responses based on a given question and retrieved context. It utilizes templates to format prompts for the AI, enabling precise and relevant answers.

## How it Works

The module extracts a question and its related context from event data, validates their presence, and formats them into a chat prompt using predefined templates. It then uses the `ChatOpenAI` interface to generate responses based on this context.

## Use Cases

- Automating customer support by providing responses that consider previous interactions or specific queries.
- Enhancing virtual assistant functionalities to offer more context-aware responses in chatbots.
- Implementing AI-driven tutoring systems where context from textbooks or lessons is used to answer student inquiries.

## Customization

- Modify the prompt templates to change the structure of the conversation or the type of responses.
- Switch the OpenAI model (e.g., from "gpt-4-turbo-preview" to another model) to vary response styles or capabilities.
- Adapt the module for different languages or domains by adjusting the chat templates and model settings.

## Environment Setup

Set the following environment variables in your Triform.ai environment:
- `OPENAI_API_KEY`: API key for OpenAI authentication.
