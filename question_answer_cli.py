#!/usr/bin/env python
# USE THE GEMINI_KEY FROM THE CODESPACE SECRETS
from google import genai
import os
import click


def ask_model(model, query):
    """Ask the model a question and print the response."""
       
        client = genai.Client(api_key="$GEMINI_KEY")
        response = client.models.generate_content(
            model=model,
            contents=query,
        )
        print(f"Response: {response.text}")


@click.command()
@click.option('--model', default='gemini', help='The model to use for the query.')
@click.option('--query', prompt='Enter your question', help='The question to ask the model.')
def main(model, query):
    """Main function to run the CLI."""
    ask_model(model, query)

if __name__ == '__main__':
    main()