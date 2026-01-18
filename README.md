# Coding Agent

A CLI-based AI coding assistant powered by Google Gemini. This agent acts as an intelligent autonomous interface that can perform file operations and execute code based on natural language commands.

## Features

- **File Operations**: List files, read content, and write/overwrite files.
- **Code Execution**: Execute Python scripts (`.py`) directly from the agent.
- **Sandboxed Environment**: Operations are safely scoped to the `./calculator` workspace directory.
- **Verbose Mode**: Optional flag to view the agent's internal thought process and tool usage.

## Prerequisites

- Python 3.12 or higher
- Google Gemini API Key

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd coding-agent

   ```

2. **Install dependencies:**
This project uses `uv` for dependency management, but standard `pip` works as well:
```bash
pip install google-genai python-dotenv

```


3. **Configure Environment:**
Create a `.env` file in the root directory and add your Gemini API key:
```text
GEMINI_API_KEY=your_actual_api_key_here

```



## Usage

Run the agent by providing a prompt as a command-line argument:

```bash
python main.py "Your prompt here"

```

**Examples:**

*List files in the workspace:*

```bash
python main.py "List all files in the directory"

```

*Generate and run code (with verbose output):*

```bash
python main.py "Write a python script to calculate the factorial of 5" --verbose

```

## Project Structure

* `main.py`: Entry point for the CLI.
* `agent_call.py`: Core logic for interacting with the Gemini API.
* `functions/`: Contains tool definitions (file I/O, code execution).
* `calculator/`: The sandboxed workspace where the agent operates.

