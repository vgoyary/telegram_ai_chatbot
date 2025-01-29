# Telegram AI Chatbot

## Overview
This project implements a Telegram chatbot that offers user registration, AI-powered chat, image/file analysis, and web search.

## Features
- User registration with phone number verification
- AI responses using Gemini
- Image and file content analysis
- AI-powered web search

## Setup
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/telegram-ai-chatbot.git
    cd telegram-ai-chatbot
    ```
    
2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # (Mac/Linux)
    venv\Scripts\activate  # (Windows)
    ```
    
3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    
4. **Configure the bot:**
    Create a `config.py` file with your API keys and MongoDB URI:
    ```python
    TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
    MONGODB_URI = "your_mongo_connection_string"
    GEMINI_API_KEY = "your_gemini_api_key"
    ```
    
5. **Run the bot:**
    ```sh
    python bot.py
    ```

## Usage
- Initiate the bot with `/start`
- Share your phone number when prompted
- Send messages to receive AI responses
- Upload images/files for analysis
- Use `/websearch <query>` to perform a web search

## Future Enhancements
- Add sentiment analysis
- Implement auto-translate for messages
- Create a dashboard for user analytics
