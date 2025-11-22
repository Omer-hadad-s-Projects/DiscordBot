from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from commands_handler import handle_command
from discord.ext import commands

load_dotenv('.env')
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
IS_DEBUG: bool = os.getenv('IS_DEBUG', 'False') == 'True'

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
command_prefix: str = '!dev_' if IS_DEBUG else '!'
bot = commands.Bot(command_prefix=command_prefix, intents=intents)

async def send_message(message: Message, user_message: str, is_debug: bool) -> None:
   
    if(send_message_check_invalid_inputs(user_message, is_debug) == False): return
    
    user_message = trim_user_message_prefix(user_message, is_debug)
    print(f'Trimmed user message: "{user_message}"')
    
    try:
        ctx = await bot.get_context(message) 
        await handle_command(ctx, user_message)
    except Exception as e:
        await message.channel.send(e)
    
        
def send_message_check_invalid_inputs(user_message: str, is_debug: bool) -> bool:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return False
    
    if(is_debug and not user_message.startswith('!dev_')):
        print('Debug mode is enabled but the message does not start with "dev"')
        return False

    if (not is_debug and not user_message.startswith('!')):
        return False

    return True
        
def trim_user_message_prefix(user_message: str, is_debug: bool) -> str:
    if(is_debug): return user_message[5:]
    else: return user_message[1:]
        
@bot.event
async def on_ready() -> None:
    debug_string = 'Debug mode is enbaled' if IS_DEBUG else ''
    print(f'{bot.user} is now running! {debug_string}')
    admin_list_str: Final[str] = os.getenv('ADMIN_LIST')
    print(f'Admin list {admin_list_str}')


@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message, IS_DEBUG)


def main() -> None:
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()
