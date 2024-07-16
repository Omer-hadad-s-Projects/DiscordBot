from discord.ext.commands import Context
from ytdlp_handler import play_audio, leave_voice_channel, is_song_playing

songsQueue : list[str] = []

async def handle_command(ctx: Context, input: str):
    if input.startswith('play'):
        await handle_command_play(ctx, input)
    elif input.startswith('stop'):
        songsQueue.clear()
        return await stop(ctx)
    elif input[0] == '!':
        raise Exception('No command found for this input')
    else: raise Exception('')
    
async def handle_command_play(ctx: Context, input: str):
    url = get_song_url_from_input(input)
    if(is_song_playing(ctx)): await add_song_to_queue(url, ctx)
    else: await play_song(ctx, url)


    
def get_song_url_from_input(input: str) -> str:
     url = input[5:]
     if(url == ''): raise ValueError("empty url")
     return url
    
async def add_song_to_queue(song_url: str, ctx: Context):
    songsQueue.append(song_url)
    print(f'Added the song to the queue, queue count: {len(songsQueue)}')
    await ctx.send(f'Added the song to the queue')
    
async def play_song(ctx: Context, url: str):
    try:
       await play_audio(ctx, url, on_song_end)
    except Exception as e:
        await ctx.send(f'An error occurred: {e} leaving voice channel')
        await leave_voice_channel(ctx)

async def on_song_end(ctx: Context):
    print(f'Song ended checking next in queue count is:{len(songsQueue)}')
    if(len(songsQueue) == 0): return
    url = songsQueue.pop(0)
    await play_song(ctx, url)
        
async def stop(ctx: Context):
    await leave_voice_channel(ctx)
    await ctx.send('Stopped the song')