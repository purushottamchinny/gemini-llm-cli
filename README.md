# Gemini LLM CLI App 🤖

A simple command-line AI application built with Python and the Google Gemini API.

This project demonstrates how to connect a Python application to a Large Language Model (LLM) using an API, send user prompts, receive AI-generated responses, and display them in the terminal.

## 🚀 Features

* Connects to the Google Gemini API
* Accepts user prompts from the terminal
* Generates AI-powered responses
* Uses environment variables to protect the API key
* Includes basic error handling
* Simple and beginner-friendly project structure

## 🛠️ Technologies Used

* Python
* Google Gemini API
* Google Gen AI Python SDK (`google-genai`)
* `python-dotenv`

## 📁 Project Structure

```text
llmapiproject/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> The `.env` file is excluded from GitHub because it contains the API key.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd llmapiproject
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Set Up the API Key

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Never upload your `.env` file or expose your API key publicly.

## ▶️ Run the Application

```bash
python main.py
```

Example:

```text
Ask AI: What is Python?

AI Response:

Python is a high-level, general-purpose programming language known for its simple and readable syntax.
```

## 🧠 How It Works

```text
User Input
    ↓
Python Application
    ↓
Gemini API Request
    ↓
Gemini LLM
    ↓
API Response
    ↓
response.text
    ↓
Terminal Output
```

The application reads the user's question using Python's `input()` function and sends it to the Gemini API using the Google Gen AI SDK.

The generated response is then extracted using `response.text` and displayed in the terminal.

## 📚 What I Learned

Through this project, I learned:

* How LLM APIs work
* How to call an LLM API using Python
* How to manage API keys using environment variables
* How to use the Google Gen AI Python SDK
* How to receive and process LLM responses
* How to handle basic API errors

## 🔮 Future Improvements

* Add continuous chat functionality
* Add conversation history
* Add system instructions
* Add structured JSON output
* Add streaming responses
* Improve error handling
* Build a web interface using Streamlit or FastAPI

## 🔐 Security

API keys should never be hard-coded directly into the Python source code.

This project uses a `.env` file to store the Gemini API key securely. The `.env` file should be included in `.gitignore`.

## 👨‍💻 Author

Purushottam N
