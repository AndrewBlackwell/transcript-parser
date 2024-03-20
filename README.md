# Transcript-Parser
Transcript-Parser is a Python-based tool designed to convert PDF academic transcripts into JSON format. Utilizing `pdftotext` for text extraction and the OpenAI API. Our tool sends the extracted transcript text to ChatGPT with a custom prompt, receiving back a structured JSON response. We also features a user interface built with Flask, providing a seamless and user-friendly way to obtain JSON-formatted academic transcripts.

Out of the box, a transcript usually requires approximately 15 seconds and incurs a cost of approximately $0.01 for every 500 tokens when using `text-davinci-002`. Consider that a standard request and response may consume 1500+ tokens (more likely around 3000 tokens).

## Requirements
- `pdftotext` for PDF text extraction
- `openai` for accessing the OpenAI API
- `flask` for creating the web interface
- `tiktoken` for managing API tokens

### Getting Started
1. Ensure Python 3 and pip3 are installed.
1. Install all dependencies of `pdftotext` (refer to [this link](https://github.com/jalan/pdftotext)).
1. Open a new terminal and, if necessary, update pip3: `python3 -m pip install --upgrade pip`
1. In another new terminal, clone the repository and navigate to the directory.
1. Verify the versions: `python3 --version` and `pip3 --version`.
1. Execute `./build.sh` in the project's root directory.
1. Obtain your [OpenAI API Key](https://openai.com/api/).
1. Create a file named `.env` and specify your API key within it: `OPENAI_API_KEY=YOURKEY`, or alternatively, set the key as an environment variable: `export OPENAI_API_KEY=YOURKEY`.
1. Run `./run.sh` in the project's root directory. The Flask server will be listening to port 5001.

