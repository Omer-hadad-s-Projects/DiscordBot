from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from responses import get_response
from discord.ext import commands

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
bot = commands.Bot(command_prefix='!', intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    try:
        ctx = await bot.get_context(message)
        response: str = await get_response(ctx ,user_message, bot)
        if response is None or response == '': 
            print('No response found for this message')
            return
        await message.channel.send(response)
    except Exception as e:
        print(e)
        
# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()
