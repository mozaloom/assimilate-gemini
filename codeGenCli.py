#!/usr/bin/env python3

import click
from olib.solutions import create_code


# creat a click group
@click.group()
def cli():
    """Generate code from comment in any language."""


# create a command to generate code from text
@cli.command()
@click.argument("comment")
@click.option("--language", default="python", help="Language to generate code in.")
def generate_code(comment, language):
    """Generate code from comment.

    example: ./codeGenCli.py generate_code "create a function that add two numbers" --language python
    """
    code = create_code(comment, language)
    click.echo(code)


if __name__ == "__main__":
    cli()
