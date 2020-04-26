import discord
import asyncio
import random
import time
import logging
import typing
from discord import Client
from discord.ext import commands
import sys, traceback
bot = commands.Bot(command_prefix=commands.when_mentioned_or('drip!'))
bot.load_extension("fun")
bot.load_extension("help")
bot.load_extension("mod")
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    activity = discord.Game(name="I hate lockdown. | drip!help", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'Successfully logged in and booted...!')
@bot.command()
async def suggest(ctx):
          emoji = '\N{THUMBS UP SIGN}'
          aemoji = '\N{THUMBS DOWN SIGN}'
          query = ctx.message.content
          stopwords = ['drip!suggest']
          querywords = query.split()
          resultwords = [word for word in querywords if word.lower() not in stopwords]
          info= ' '.join(resultwords)     
          embed = discord.Embed(title="Suggestion!", description=info, colour=0x00ff00)
          embed.add_field(name="Suggester", value=ctx.author, inline=False)
          channel = bot.get_channel(703576457145745452)
          await channel.send(embed=embed)
          await ctx.message.add_reaction(emoji)
          await ctx.messageObject.add_reaction(emoji)
          await ctx.messageObject.add_reaction(aemoji) 
@bot.event
async def on_guild_join():
    embed = discord.Embed(title="Thanks for adding me!", description="My name is SobbleBot, Agent SobbleBot. ")    
    embed.add_field(name="Operation Join Server is accomplished.", description="https://cdn.discordapp.com/attachments/336642776609456130/648509688480268308/5025d60f9100f844d6294c3d6c2e32c8-1.png")   
    await ctx.send(embed=embed)     
@bot.event    
async def on_message(message):
 if message.author == bot.user:
      return
 if message.content.startswith('<@645009678224457740>'):    
     await message.channel.send("Use drip!help to find all the commands!")
 await bot.process_commands(message)
bot.run('NzAzNTg1OTM0OTEzODMwOTcy.XqWfXA.6IeBLThZvoa1SQlDA-7kiIK-j-A')
