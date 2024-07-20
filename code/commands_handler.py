from discord.ext.commands import Context
from ytdlp_handler import play_audio, leave_voice_channel, get_info

songsQueue : list[dict] = []
is_song_playing : bool = False

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
    info = get_info(url)
    if(is_song_playing): await add_song_to_queue(ctx, info)
    else: await play_song(ctx, info)


    
def get_song_url_from_input(input: str) -> str:
     url = input[5:]
     if(url == ''): raise ValueError("empty url")
     return url
    
async def add_song_to_queue(ctx: Context, info: dict):
    songsQueue.append(info)
    print(f'Added the song to the queue, queue count: {len(songsQueue)}')
    title = info['title']
    await ctx.send(f"Added **{title}** to the queue")
    
async def play_song(ctx: Context, info: dict):
    global is_song_playing
    try:
       is_song_playing = True
       await play_audio(ctx, info, on_song_end)
    except Exception as e:
        await ctx.send(f'An error occurred: {e} leaving voice channel')
        await leave_voice_channel(ctx)
        is_song_playing = False
        

async def on_song_end(ctx: Context):
    global is_song_playing
    print(f'Song ended checking next in queue count is:{len(songsQueue)}')
    if(len(songsQueue) == 0): 
        is_song_playing = False
        await ctx.send('No more songs in queue, leaving voice channel')
        await leave_voice_channel(ctx)
    else:
        info = songsQueue.pop(0)
        await play_song(ctx, info)
        
async def stop(ctx: Context):
    await leave_voice_channel(ctx)
    await ctx.send('Stopped the song')