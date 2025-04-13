from openai import OpenAI
import os

""" library of openai solutions """


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
    return response.choices[0].message.content


# build a function that convert comment into code in any language
def create_code(comment, language="python"):
    """Function to create code from comment."""
    client = OpenAI(
        api_key=os.getenv("GEMINI_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that convert comment into {language} code."},
            {"role": "user", "content": comment},
        ],
    )
    return response.choices[0].message.content



