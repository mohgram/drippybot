import discord
from discord.ext import commands
class help(commands.Cog):
 def __init__(self, bot):
  self.bot = bot
  bot.remove_command('help')
 @commands.command()
 async def help(self, ctx):
    embed = discord.Embed(title="Here's your help help!", description="This is the help command help page!")
    embed.add_field(name="fhelp_[pagenumber]", value="The main aspect of the bot, fun!", inline=False)
    embed.add_field(name="mhelp", value="The 2nd aspect of the bot, moderation!", inline=False)
    embed.add_field(name="dhelp", value="Help for DBL commands!", inline=False)
    embed.add_field(name="faq", value="Frequently Asked Questions", inline=False)
    await ctx.send(embed=embed)
 @commands.command()
 async def fhelp_1(self, ctx):
        embed = discord.Embed(title="Here's your fun help!", description="Page 1 of 3", color=0x206694)
        embed.add_field(name="fhelp", value="Help is brought up", inline=False)
        embed.add_field(name="suggest [suggestion]", value="Suggests an idea to be added to SobbleBot", inline=False)
        embed.add_field(name="calmingmusic", value="Gives you a video of calming waves.", inline=False)
        embed.add_field(name="dab", value="?????", inline=False)
        embed.add_field(name="story", value="tells you a nice little story with you as the main character!", inline=False)
        await ctx.send(embed=embed)
 @commands.command() 
 async def fhelp_2(self, ctx):
        embed = discord.Embed(title="Here's your fun help!", description="Page 2 of 3")            
        embed.add_field(name="wisdom", value="Random wisdom.", inline=False)
        embed.add_field(name="eightball", value="An 8ball function that sees the future.", inline=False)
        embed.add_field(name="dice",value="Guess a number of 6, if the computer sees the same, you win!", inline=False)
        embed.add_field(name='coinflip', value="It flips a coin.", inline=False)
        embed.add_field(name="joke", value="Tells you a funny joke.", inline=False)
        await ctx.send(embed=embed)
 @commands.command()
 async def fhelp_3(self, ctx):
        embed = discord.Embed(title="Here's your help!", description="This is page 3 of Fun Help!For page one, do drip!fhelp!")        
        embed.add_field(name="highfive", value="High five!", inline=False)
        embed.add_field(name="vanish", value="Provides a vanishing GIF.", inline=False)
        embed.add_field(name="dance", value="Provides a dancing GIF", inline=False)
        embed.add_field(name="randmeme", value="Gives you a meme out of an ever growing list", inline=False)
        embed.add_field(name="drift", value="kansei dorifto!", inline=False)
        await ctx.send(embed=embed)
 @commands.command()
 async def mhelp(self, ctx, arg):
    embed = discord.Embed(title="Here's your moderation help!", description="Moderation help is here!")
    embed.add_field(name="sbban", value="Bans a user", inline=False)
    embed.add_field(name="sbunban", value="Unbans a user", inline=False)
    embed.add_field(name="sbmute", value="Mutes a user[creates a role called muted]", inline=False)
    embed.add_field(name="sbunmute", value="Unmutes a user", inline=False)
    await ctx.send(embed=embed)
 @commands.command()
 async def faq(self, ctx):
    embed = discord.Embed(title="Here's your SobbleBot FAQ!", description="Frequently asked questions")
    embed.add_field(name="Who made this bot?", value="lilugug did!", inline=False)
    embed.add_field(name="What's the support server?", value="https://discord.gg/8uQ4EeX", inline=False)
    await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))