import discord
import yt_dlp

def is_song_playing(ctx):
    return ctx.voice_client.is_playing()

async def play_audio(ctx, url):
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()

    FFMPEG_OPTIONS =FFMPEG_OPTIONS ={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.5"'}
    
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'quiet': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        secret = url
        info = ydl.extract_info(secret, download=False)
        url2 = info['url']
        print(url2)
        source = discord.FFmpegOpusAudio(url2, **FFMPEG_OPTIONS)
        vc = ctx.voice_client
        vc.play(source)
        
async def leave_voice_channel(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()