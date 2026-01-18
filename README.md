```markdown
# Coding Agent

A CLI-based AI coding assistant powered by Google Gemini. This agent acts as an intelligent autonomous interface that can perform file operations and execute code based on natural language commands.

## Features
* **File Operations**: List files, read content, and write/overwrite files.
* **Code Execution**: Execute Python scripts (`.py`) directly from the agent.
* **Sandboxed Environment**: Operations are currently scoped to the `./calculator` workspace directory.
* **Verbose Mode**: Optional flag to view the agent's internal thought process and tool usage.

## Prerequisites
* Python 3.12 or higher
* Google Gemini API Key

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd coding-agent
    ```

2.  **Install dependencies:**
    This project uses `uv` for dependency management, but you can also use pip:
    ```bash
    pip install google-genai python-dotenv
    ```

3.  **Configure Environment:**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```text
    GEMINI_API_KEY=your_actual_api_key_here
    ```

## Usage

Run the agent by providing a prompt as a command-line argument:

```bash
python main.py "Your prompt here"

```

**Example:**

```bash
python main.py "Write a python script to calculate the factorial of 5" --verbose

```

```

***

### Step-by-Step Commands for Local Use

Follow these simple commands in your terminal to get the project running on your local device:

**Step 1: Enter the project folder**
```bash
cd coding-agent

```

**Step 2: Create the configuration file**
*(On Windows, use `type NUL > .env` instead of touch)*

```bash
touch .env

```

**Step 3: Add your API Key**
Open the `.env` file you just created with a text editor (like Notepad or VS Code) and paste your Google GenAI key inside it like this:
`GEMINI_API_KEY=AIzaSyD...`

**Step 4: Install the required libraries**

```bash
pip install google-genai python-dotenv

```

**Step 5: Run the Agent**
You can now ask the agent to perform tasks. For example, to list files in the workspace:

```bash
python main.py "List all files in the directory"

```
