import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command
import openai



load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TELEGRAM_TOKEN = getenv("TELEGRAM-BOT-TOKEN")
openai.api_key=getenv("OPENAI-API-KEY")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

# Create a Router instance
router = Router()

class Reference:
    def __init__(self):
        self.reference=""

reference=Reference()


def clear_chat():
    reference.reference=""


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\nHow can I assist you today?")

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    help_text = """
    Available commands:
    - /start: Greet the user
    - /help: Show this help message
    - /clear: Clear the chat history 
    """
    await message.answer(help_text)

@dp.message(Command("clear"))
async def command_clear_handler(message: Message) -> None:
    """
    This handler receives messages with `/clear` command

    """
    clear_chat()
    await message.answer("The chat History has been cleared.")

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Echo handler for all other messages with OpenAI integration
    """
    try:
        # Send the user's message to OpenAI and get a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": reference.reference},
                {"role": "user", "content": message.text}
            ]
        )

        # Extract and send the AI-generated response
        ai_response = response["choices"][0]["message"]["content"]
        reference.reference+=ai_response
        await message.answer(ai_response)
    except Exception as e:
        # Handle any errors (e.g., API errors)
        await message.answer(f"An error occurred: {str(e)}")

async def main() -> None:
    # Initialize Bot instance
    bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Attach the router to the dispatcher
    dp.include_router(router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
