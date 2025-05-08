# Simple Python Chatbot

A simple chatbot application written in Python, featuring both a command-line interface and a web interface.

## Features

- Pattern-based response system
- Command-line interface
- Web interface using Flask
- No external APIs or AI models required

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

To run the chatbot in the command line:

```bash
python chatbot.py
```

### Web Interface

To run the chatbot with a web interface:

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000` to interact with the chatbot.

## How It Works

This chatbot uses regular expressions to match patterns in user input and responds with predefined messages. It's a very simple approach but demonstrates the basic structure of a chatbot application.

The chatbot currently understands prompts like:
- Greetings (hello, hi, hey)
- Questions about itself (what is your name, who made you)
- Basic conversation (how are you, thank you)
- Requests (tell me a joke)
- Farewells (bye, goodbye)

## Customization

You can easily extend the chatbot by adding more patterns and responses to the `responses` dictionary in the `SimpleChatbot` class in `chatbot.py`.

## Requirements

- Python 3.6 or higher
- Flask (for the web interface) 