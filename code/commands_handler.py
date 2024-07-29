from discord.ext.commands import Context
from ytdlp_handler import play_audio, leave_voice_channel, get_info, stop_song_playing
from admin_utility import get_admin_list, check_is_admin_locked, activate_admin_lock, deactivate_admin_lock

PLAY_COMMAND = 'play'
HELP_COMMAND = 'help'
STOP_COMMAND = 'stop'
NEXT_COMMAND = 'next'
REMOVE_COMMAND = 'remove'
NEXT_SONGS_COMMAND = 'next_songs'
ADMIN_LOCK_COMMAND = 'admin_lock'

next_songs_list : list[dict] = []
is_song_playing : bool = False
admin_lock_commands: list[str] = [STOP_COMMAND, NEXT_COMMAND, REMOVE_COMMAND]

async def handle_command(ctx: Context, input: str):
    command = get_command_from_input(input)
    arguments = get_command_arguments(input)
    
    if check_command_locked(ctx, command):
        await ctx.send('Only admin can use this command in locked mode')
        return
    if command == ADMIN_LOCK_COMMAND:
        await toggle_admin_lock(ctx)
    elif command == PLAY_COMMAND:
        await play_song_command(ctx, arguments)
    elif command == HELP_COMMAND:
        await send_help_text(ctx)
    elif command == STOP_COMMAND:
        await stop(ctx)
    elif command == NEXT_COMMAND:
        await next_song(ctx)
    elif command == NEXT_SONGS_COMMAND:
        await print_next_songs(ctx)
    elif command == REMOVE_COMMAND:
        await remove_song(ctx, arguments)
    else:
        await ctx.send('Invalid command, type !help to see the list of commands')
        
def get_command_from_input(input: str) -> str:
    return input.split(' ')[0]

def get_command_arguments(input: str) -> list[str]:
    return input.split(' ')[1:]
    
def check_command_locked(ctx: Context, command: str) -> bool:
    if(is_admin(ctx) or not check_is_admin_locked()):
        return False
    return admin_lock_commands.__contains__(command)

async def toggle_admin_lock(ctx: Context):
    if(not is_admin(ctx)):
        await ctx.send('Only admin can toggle admin lock')
        return
    if(check_is_admin_locked()):
        deactivate_admin_lock()
        await ctx.send('Admin lock now deactivated')
    else:
        activate_admin_lock()
        await ctx.send('Admin lock activated')

def is_admin(ctx: Context):
    sender_id = ctx.author.id
    admin_list = get_admin_list()
    return admin_list.__contains__(sender_id)
    
async def play_song_command(ctx: Context, arguments: list[str]):
    url = arguments[0]
    if(url == None): 
        await ctx.send('Please provide a valid url')
        return
    info = get_info(url)
    if(is_song_playing): await add_song_to_queue(ctx, info)
    else: await play_song(ctx, info)
    
async def add_song_to_queue(ctx: Context, info: dict):
    next_songs_list.append(info)
    print(f'Added the song to the queue, queue count: {len(next_songs_list)}')
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
    print(f'Song ended checking next in queue count is:{len(next_songs_list)}')
    if(len(next_songs_list) == 0): 
        is_song_playing = False
        await ctx.send('No more songs in queue, leaving voice channel')
        await leave_voice_channel(ctx)
    else:
        info = next_songs_list.pop(0)
        await play_song(ctx, info)

async def next_song(ctx: Context):
    if(len(next_songs_list) == 0): return await ctx.send('No more songs in queue')
    await stop_song_playing(ctx)

async def print_next_songs(ctx: Context):
    if(len(next_songs_list) == 0): return await ctx.send('No more songs in queue')
    songs = ''
    for i, song in enumerate(next_songs_list):
        title = song['title']
        songs += f'{i+1}. {title}\n'
    await ctx.send(f'{songs}')
        
async def stop(ctx: Context):
    next_songs_list.clear()
    await leave_voice_channel(ctx)
    await ctx.send('Stopped the song')
    
async def send_help_text(ctx: Context):
    file = open('help.txt', 'r')
    content = file.read()
    await ctx.send(content)

async def remove_song(ctx: Context, arguments: list[str]):
    if(len(next_songs_list) == 0):
        await ctx.send('No songs in queue to remove')
        return
    
    song = arguments[0]
    if(song is None):
        await ctx.send('No song number was provided')
        return
    
    try:
        intValue = int(song)
    except ValueError:
        await ctx.send('Invalid input, you need to add the song number that you want to remove')
        return
    
    if(len(next_songs_list) + 1 < intValue):
        await ctx.send(f'There is not song number {intValue} in the queue')   
    else:
        del next_songs_list[intValue - 1]
        await ctx.send(f'Song number {intValue} in queue was removed')
  

    