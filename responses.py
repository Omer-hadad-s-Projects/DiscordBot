from discord.ext.commands import Context
from discord.ext import commands
from ytdlp_handler import play_audio, leave_voice_channel

async def get_response(ctx: Context, input: str) -> str:
    if input.startswith('play'):
        return await play_song(ctx, input)
    elif input.startswith('pause'):
        return 'Paused the song'
    elif input.startswith('stop'):
        return await stop(ctx)
    elif input[0] == '!':
        return 'No command found for this input'
    else: return ''
    
async def play_song(ctx: Context, input: str) -> str:
    url = input[6:]
    if(url == ''):
        return 'No URL found'
    try:
       await play_audio(ctx, url)
       return 'Playing the song'
    except Exception as e:
        await leave_voice_channel(ctx)
        return f'Error {e}'

async def stop(ctx: Context):
    await leave_voice_channel(ctx)
    return 'Stopped the song'