import asyncio
import discord
import yt_dlp

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

ydl = yt_dlp.YoutubeDL(ydl_opts)

def get_info(url):
        info = ydl.extract_info(url, download=False)
        return info

async def play_audio(ctx, info, on_song_end):
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()

    def after_playing(error):
        if error:
          print(f"An error occurred: {error}")
        else:
            print("Song has finished playing.")
        # Call the on_song_end function here
        asyncio.run_coroutine_threadsafe(on_song_end(ctx), ctx.bot.loop)
    
    song_title = info['title']
    await ctx.send(f'Playing {song_title}')
    playUrl = info['url']
    print(playUrl)
    source = discord.FFmpegOpusAudio(playUrl, **FFMPEG_OPTIONS)
    vc = ctx.voice_client
    vc.play(source, after=after_playing)
            
async def leave_voice_channel(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()