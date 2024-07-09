import discord
import yt_dlp
from discord.ext import commands
from discord.ext.commands import Context

# Function to join voice channel
async def join_voice_channel(ctx: Context):
    channel = ctx.author.voice.channel
    if channel:
        await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel to use this command.")

# Function to play audio from YouTube
async def play_audio(ctx: Context, url: str, bot:commands.Bot):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url = info['formats'][0]['url']  # URL of the audio stream
    
    voice_client.play(discord.FFmpegPCMAudio(url), after=lambda e: print('done', e))

# Function to leave voice channel
async def leave_voice_channel(ctx: Context, bot: commands.Bot):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("I'm not connected to a voice channel.")


