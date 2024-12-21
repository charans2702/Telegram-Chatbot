# Telegram OpenAI Chatbot

A Telegram bot that integrates with OpenAI's GPT-3.5-turbo model to provide intelligent responses to user messages. The bot maintains conversation context and includes basic command functionality.

## Features

- Integration with OpenAI's GPT-3.5-turbo model
- Conversation context maintenance
- Basic command handling (/start, /help, /clear)
- Error handling for API responses
- Environment variable configuration for secure token management

## Prerequisites

- Python 3.7 or higher
- A Telegram Bot Token (obtained from [@BotFather](https://t.me/BotFather))
- An OpenAI API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/charans2702/Telegram-Chatbot.git
cd Telegram-Chatbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your credentials:
```
TELEGRAM-BOT-TOKEN=your_telegram_bot_token_here
OPENAI-API-KEY=your_openai_api_key_here
```

## Usage

1. Start the bot:
```bash
python main.py
```

2. Open Telegram and search for your bot using its username.

3. Available commands:
   - `/start` - Initiates the conversation with a greeting
   - `/help` - Displays available commands
   - `/clear` - Clears the conversation history

4. Send any message to interact with the OpenAI-powered chatbot



## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## Acknowledgments

- [Aiogram](https://github.com/aiogram/aiogram) for the Telegram Bot framework
- [OpenAI](https://openai.com/) for the GPT-3.5-turbo model