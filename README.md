# AI Agent Boot

This is a project based on boot.dev, it's not purely my work, but it was an interesting experience. And this README is also an experience with an AI agent, hahah :-)

## Features

- **Intelligent Code Analysis**: Automatically explores and understands project structures
- **File Operations**: Read file contents, list directory structures, and write new files
- **Python Execution**: Run Python scripts and verify code functionality
- **AI-Powered Assistance**: Uses Google's Gemini 2.5 Flash model for intelligent responses
- **Safe Execution**: Operates within a confined working directory for security
- **Tool-Based Workflow**: Follows a systematic approach using specialized tools

## Installation

### Prerequisites

- Python 3.14 or higher
- Google Gemini API key

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-agent-boot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or if using pyproject.toml
   pip install .
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the AI agent with a prompt:

```bash
python main.py "Analyze the calculator module and suggest improvements"
```

### Command Line Options

- `user_prompt`: The task or question for the AI agent
- `--verbose`: Enable detailed output of function calls and responses

### Example Usage

```bash
# Analyze a project
python main.py "Review the calculator package and identify potential bugs"

# Generate documentation
python main.py "Create documentation for the functions in the functions directory"

# Run tests
python main.py "Execute all tests in the calculator/tests.py file"
```

## Configuration

The agent operates within the `calculator` directory by default. You can modify the working directory in the system prompt if needed.

Key configuration files:
- `config.py`: Contains settings like `MAX_CHARS` for file reading limits
- `prompts.py`: Defines the system prompt and agent behavior

## Project Structure

```
ai-agent-boot/
├── main.py                 # Main entry point for the AI agent
├── config.py              # Configuration settings
├── prompts.py             # System prompts and instructions
├── call_function.py       # Function calling utilities
├── pyproject.toml         # Project metadata and dependencies
├── calculator/            # Working directory for the agent
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
└── functions/             # Available tools for the agent
    ├── get_file_content.py
    ├── get_files_info.py
    ├── run_python_file.py
    └── write_file.py
```

## Available Tools

The AI agent has access to the following tools:

- **get_files_info**: Lists files and directories in a given path
- **get_file_content**: Reads and returns file contents (up to MAX_CHARS limit)
- **run_python_file**: Executes Python scripts and returns output
- **write_file**: Creates or modifies files

## How It Works

1. The agent receives a user prompt
2. It uses available tools to gather information about the project
3. Analyzes code, runs tests, and performs requested tasks
4. Provides intelligent responses based on the gathered data
5. Can iteratively refine its understanding through multiple tool calls

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for development assistance and should be used responsibly. Always review AI-generated code before using it in production environments.