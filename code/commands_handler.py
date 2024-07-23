from discord.ext.commands import Context
from ytdlp_handler import play_audio, leave_voice_channel, get_info, stop_song_playing
from url_utility import is_valid_url

nextSongsList : list[dict] = []
is_song_playing : bool = False

async def handle_command(ctx: Context, input: str):
    if input.startswith('play'):
        await handle_command_play(ctx, input)
    elif input == 'stop':
        return await stop(ctx)  
    elif input == 'next':
        await next(ctx)
    elif input == 'next songs':
        await print_next_songs(ctx)
    elif input == 'help':
        await send_help_text(ctx)
    else: await ctx.send('Invalid command, type !help to see the list of commands')
    
async def handle_command_play(ctx: Context, input: str):
    url = await get_song_url_from_input(input)
    if(url == None): 
        await ctx.send('Please provide a valid url')
        return
    info = get_info(url)
    if(is_song_playing): await add_song_to_queue(ctx, info)
    else: await play_song(ctx, info)
    
async def get_song_url_from_input(input: str) -> str:
     url = input[5:]
     if(not is_valid_url(url)): return None
     return url
    
async def add_song_to_queue(ctx: Context, info: dict):
    nextSongsList.append(info)
    print(f'Added the song to the queue, queue count: {len(nextSongsList)}')
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
    print(f'Song ended checking next in queue count is:{len(nextSongsList)}')
    if(len(nextSongsList) == 0): 
        is_song_playing = False
        await ctx.send('No more songs in queue, leaving voice channel')
        await leave_voice_channel(ctx)
    else:
        info = nextSongsList.pop(0)
        await play_song(ctx, info)

async def next(ctx: Context):
    if(len(nextSongsList) == 0): return await ctx.send('No more songs in queue')
    await stop_song_playing(ctx)

async def print_next_songs(ctx: Context):
    if(len(nextSongsList) == 0): return await ctx.send('No more songs in queue')
    songs = ''
    for i, song in enumerate(nextSongsList):
        title = song['title']
        songs += f'{i+1}. {title}\n'
    await ctx.send(f'{songs}')
        
async def stop(ctx: Context):
    nextSongsList.clear()
    await leave_voice_channel(ctx)
    await ctx.send('Stopped the song')
    
async def send_help_text(ctx: Context):
    #print help text from file help.txt 
    file = open('help.txt', 'r')
    content = file.read()
    await ctx.send(content)
    