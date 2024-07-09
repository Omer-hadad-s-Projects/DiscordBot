from yt_dlp_handler import join_voice_channel, play_audio, leave_voice_channel
from discord.ext.commands import Context
from discord.ext import commands

async def get_response(ctx: Context, input: str, bot: commands.Bot) -> str:
    if input.startswith('!play'):
        return await PlaySong(ctx, input, bot)
    elif input.startswith('!pause'):
        return 'Paused the song yamaniac'
    elif input.startswith('!stop'):
        return await Stop(ctx, bot)
    elif input[0] == '!':
        return 'No command found for this input yamaniac'
    else: return ''
    
async def PlaySong(ctx: Context, input: str, bot: commands.Bot) -> str:
    url = input[6:]
    if(url == ''):
        return 'No URL found yamaniac'
    try :
        await join_voice_channel(ctx)
        await play_audio(ctx, url, bot)
        return 'Playing the song yamaniac'
    except:
        await leave_voice_channel(ctx, bot)
        return 'Error yamaniac'

async def Stop(ctx: Context, bot: commands.Bot):
    await leave_voice_channel(ctx, bot)
    return 'Stopped the song yamaniac'

    