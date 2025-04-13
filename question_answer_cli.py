#!/usr/bin/env python

import click
from olib.solutions import ask_model


@click.command()
@click.option(
    "--query", prompt="Enter your question", help="The question to ask the model."
)
def main(query):
    """Main function to run the CLI."""
    # Ensure the query is passed to ask_model
    ask_model(query)


if __name__ == "__main__":
    # pylint: disable=E1120
    main()
