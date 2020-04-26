import discord
import typing
import time
import asyncio
from discord.ext import commands
class mod(commands.Cog):
 def __init__(self, bot):
        self.bot = bot
 async def on_command_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
           await ctx.send("There's no right for you to be using this command!(Missing Permissions)")
 @commands.command()
 @commands.has_permissions(kick_members=True)
 async def kick(self, ctx, member : discord.Member, *, reason=None):
  if member is None:
      await ctx.send("Please input an actual person!")
  else:         
   await member.kick(reason=reason)
   await ctx.send("GAME! That user's been kicked.")  
 @commands.command()
 @commands.has_permissions(ban_members=True)
 async def unban(self, ctx, member : discord.Member, * , reason=None): 
  if member is None:    
      await ctx.send("There's no user to unban!")
  else:      
   await member.unban(reason=reason)
   await ctx.send("*door opens* That user has been unbanned")
 @commands.command() 
 @commands.has_permissions(ban_members=True)
 async def ban(self, ctx, member : discord.Member, *, reason=None): 
  if member is None:    
      await ctx.send("There's no user to ban!")
  else:      
   await member.ban(reason=reason)
   await ctx.send("*door shuts* That user has been banned")
 @commands.command() 
 @commands.has_permissions(ban_members=True)
 async def softban(self, ctx, member : discord.Member, time, *, reason=None): 
  if member is None:    
      await ctx.send("There's no user to ban!")
  else:      
   await member.ban(reason=reason)
   await ctx.send("*door shuts* That user has been banned")
   await asyncio.sleep(time)
   await member.unban(reason="times up")
 @commands.command()
 @commands.has_permissions(kick_members=True)
 async def mute(self, ctx, member : discord.Member):
    guild = ctx.guild
    for role in guild.roles:
       if role.name == "Muted":
        await member.add_roles(role)
        await ctx.send(f"{member.name} was muted")
    if member is None:
        await ctx.send("please pass in a valid user")
        return
 @commands.command()
 @commands.has_permissions(kick_members=True)
 async def tempmute(self, ctx, member : discord.Member, time, *,reason=None):
    guild = ctx.guild
    for role in guild.roles:
       if role.name == "Muted":
        await member.add_roles(role)
        await ctx.send(f"{member.name} was muted")
    if member is None:
        await ctx.send("please pass in a valid user")
        return
        await asyncio.sleep(time)
        await ctx.send(f"{member.name} was unmuted")
        await member.remove_roles(role)
 @commands.command()
 @commands.has_permissions(kick_members=True)
 async def unmute(self, ctx, member : discord.Member = None, *, reason=None):
    guild = ctx.guild
    for role in guild.roles:
       if role.name == "Muted":
        await member.remove_roles(role)
        await ctx.send(f"{member.name} was unmuted")
    if member is None:
        await ctx.send('Please pass in a valid user')
        return
 @commands.command()
 async def joined(self, ctx, member: discord.Member):
    embed = discord.Embed(name="When did they join?", description="Hmm when did they join?")
    embed.add_field(name="Let's see... oh I know!", value="{0.name} joined in {0.joined_at}!".format(member))
    embed.add_field(name="The time system", value="It's YYYY-MM-DD")
    await ctx.send(embed=embed)   
def setup(bot):
    bot.add_cog(mod(bot))