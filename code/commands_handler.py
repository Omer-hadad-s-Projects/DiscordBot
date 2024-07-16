from discord.ext.commands import Context
from ytdlp_handler import play_audio, leave_voice_channel, is_song_playing

songsQueue : list[str] = []

async def handle_command(ctx: Context, input: str):
    if input.startswith('play'):
        url = get_song_url_from_input(input)
        print(f'URL: {url}')
        print(f'Ctx: {ctx == None} {ctx.voice_client == None}')
        if(is_song_playing(ctx)): add_song_to_queue(url)
        else: play_song(ctx, url)
    elif input.startswith('pause'):
        ctx.send('Paused the song')
    elif input.startswith('stop'):
        return await stop(ctx)
    elif input[0] == '!':
        raise Exception('No command found for this input')
    else: raise Exception('')
    
def get_song_url_from_input(input: str) -> str:
     url = input[6:]
     if(url == ''): raise ValueError("empty url")
    
def add_song_to_queue(song_url: str, ctx: Context):
    songsQueue.append(song_url)
    ctx.send(f'Added the song to the queue')
    
async def play_song(ctx: Context, url: str):
    try:
       ctx.send('Playing the song')
       await play_audio(ctx, url)
    except Exception as e:
        ctx.send(f'An error occurred: {e} leaving voice channel')
        await leave_voice_channel(ctx)
        
async def stop(ctx: Context):
    await leave_voice_channel(ctx)
    ctx.send('Stopped the song')