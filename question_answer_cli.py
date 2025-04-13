#!/usr/bin/env python
# USE THE GEMINI_KEY FROM THE CODESPACE SECRETS

from openai import OpenAI
import os
import click


def ask_model(query):
    """Function to ask the model a question."""
    client = OpenAI(
        api_key=os.getenv("GEMINI_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
        ],
    )

    # Access the content attribute directly
    print(response.choices[0].message.content)


@click.command()
@click.option(
    "--query", prompt="Enter your question", help="The question to ask the model."
)
def main(query):
    """Main function to run the CLI."""
    # Ensure the query is passed to ask_model
    ask_model(query)


if __name__ == "__main__":
    main(None)
