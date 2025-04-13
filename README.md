[![Python application test with Github Actions using devcontainers](https://github.com/mozaloom/assimilate-gemini/actions/workflows/main.yml/badge.svg)](https://github.com/mozaloom/assimilate-gemini/actions/workflows/main.yml)
# Assimilate Gemini API

Assimilate Gemini is a Python-based project that leverages Gemini API and OpenAI libraries to provide intelligent solutions for question answering and code generation. The repository includes both CLI and web-based applications for interacting with the Gemini API.

## Features

- **Question Answering**: Ask questions and get intelligent answers using the Gemini API.
- **Code Generation**: Generate code snippets in various programming languages based on user-provided prompts.
- **CLI Tools**: Command-line interfaces for both question answering and code generation.
- **Web Applications**: Streamlit-based web apps for an interactive user experience.

## Requirements

- Python 3.12 or higher
- An OpenAI Gemini API key (set as the `GEMINI_KEY` environment variable)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mozaloom/assimilate-gemini.git
   cd assimilate-gemini
   ```

2. Build the development environment:
   ```bash
   make install
   ```

3. Set the `GEMINI_KEY` environment variable:
   ```bash
   export GEMINI_KEY="your_openai_api_key"
   ```

## Usage

### CLI Applications

#### Question Answering CLI
Run the CLI to ask questions:
```bash
./question_answer_cli.py --query "What is the capital of France?"
```

#### Code Generation CLI
Generate code snippets from comments:
```bash
./codeGenCli.py generate_code "Create a function that adds two numbers" --language python
```

### Web Applications

#### Question Answering Web App
Run the Streamlit app for question answering:
```bash
streamlit run question_answer_webapp.py
```

#### Code Generation Web App
Run the Streamlit app for code generation:
```bash
streamlit run codeGenWebApp.py
```

## Development

### Linting
Run `pylint` to check for code quality:
```bash
make lint
```

### Testing
Run `pytest` to execute unit tests:
```bash
make test
```

### Formatting
Use `black` to format the code:
```bash
make format
```

## File Structure

- `question_answer_cli.py`: CLI for question answering.
- `codeGenCli.py`: CLI for code generation.
- `question_answer_webapp.py`: Web app for question answering.
- `codeGenWebApp.py`: Web app for code generation.
- `olib/solutions.py`: Core library for interacting with the Gemini API.
- `test_oai_solutions.py`: Unit tests for the `olib/solutions.py` library.
- `Makefile`: Automation for installation, linting, testing, and formatting.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgments

- [OpenAI](https://openai.com/) for the Gemini API.
- [Streamlit](https://streamlit.io/) for the web application framework.
- [Click](https://click.palletsprojects.com/) for building CLI tools.