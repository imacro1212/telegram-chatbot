# Telegram Chatbot

This project is a Telegram bot that provides users with the coordinates of a given place. It utilizes the Telegram Bot API to interact with users and a geocoding service to fetch location data.

## Features

- Responds to user input with the coordinates of specified places.
- Continuously runs to listen for user messages.

## Project Structure

```
telegram-chatbot
├── src
│   ├── bot.py          # Main entry point for the Telegram bot
│   └── utils
│       └── location.py # Utility functions for handling location data
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/telegram-chatbot.git
   cd telegram-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot by talking to [BotFather](https://t.me/botfather) and obtain your bot token.

4. Update the bot token in `src/bot.py`.

## Usage

To run the bot, execute the following command:
```
python src/bot.py
```

Once the bot is running, you can send a message with a place name, and it will respond with the corresponding coordinates.

## License

This project is licensed under the MIT License.