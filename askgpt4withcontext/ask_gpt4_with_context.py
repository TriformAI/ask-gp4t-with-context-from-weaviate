import os
import json

from langchain_openai import ChatOpenAI  # Interface to OpenAI's Chat models.
from langchain_core.prompts.chat import (
    ChatPromptTemplate,  # For crafting chat-based prompts.
    SystemMessagePromptTemplate,  # For creating system messages in chat prompts.
)

OPENAI_API_KEY = os.environ[
    "OPENAI_API_KEY"
]  # Securely fetch OpenAI API key from environment variables.


def handler(event, context):
    # Extract the question and context from the event object.
    question = event.get("question")
    retrieved_context = event.get("retrieved_context")

    # Validate presence of question and context.
    if not question:
        return {"error": "No question provided"}
    if not retrieved_context:
        return {"error": "No retrieved context provided"}

    # Template for the chat where the model plays the role of an assistant using provided context.
    template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
    Question: {question}
    Context: {context}
    Answer:
    """
    # Create a system message prompt from the predefined template.
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # Prepare the chat prompt with the system message.
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    # Initialize the ChatOpenAI object with model specifications and API key.
    llm = ChatOpenAI(
        model_name="gpt-4-turbo-preview", temperature=0, openai_api_key=OPENAI_API_KEY
    )

    # Generate a chat completion using the prepared prompt, formatted with actual context and question.
    response = llm.invoke(
        chat_prompt.format_prompt(
            context=retrieved_context, question=question
        ).to_messages()
    )

    # Return the model's response as a JSON-formatted string.
    return json.dumps({"output_0": response.content})
