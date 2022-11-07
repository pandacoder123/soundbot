import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import json


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="x",intents=intents)
# intents = discord.Intents.default()
# intents.members = True

# client = commands.Bot(command_prefix= '!', intents=intents)

@client.event
async def on_ready():
    print('bot is online')

@client.command()
async def hello(ctx):
    await ctx.send('Hello,,')

@client.event
async def on_member_join(member):
    channel = client.get_channel('1025257790572343299')
    await channel.send('hello')

@client.event
async def on_member_remove(member):
    channel = client.get_channel('1025257790572343299')
    await channel.send('bye')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="ff.exe", source="apple.mp3"))
        # source = FFmpegPCMAudio('apple.mp3')
        # player = voice.play(source)
        # player()

    else:
        await ctx.send('you are not in vc, you need to be in vc to run this command')

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.author.voice):
        await ctx.guild.voice_client.dissconnect()
        await ctx.send("I left vc")
    else:
        await ctx.send('I am not in a vc')

client.run('MTAzOTAwMzYwNjg5NDAwNjMyMw.GAKn4g.1KmRbbs61sINwfT0QHjiKDwkziAuy9P5trkECY')