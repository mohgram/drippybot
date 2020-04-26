import discord
from discord.ext import commands
class FunCog(commands.Cog):
 def __init__(self, bot):
    self.bot = bot
 @commands.command()
 async def calmingmusic(self, ctx):
    await ctx.send("***https://www.youtube.com/watch?v=j5a0jTc9S10***")
 @commands.command()
 async def wisdom(self, ctx):
    wisdom = ["You can't get banned from a server if you follow the rules.","A sort of life is better than no life.","Some servers aren't worth going to.","Don't obsess over everything."]
    wisdomc = random.choice(wisdom)
    await ctx.send(wisdomc)
 @commands.command()
 async def eightball(self, ctx): 
        messag = ["Yes.", "It is certain", "Probably", "50/50", "There is a low probability.", "No."]
        message = random.choice(messag)
        await ctx.send(message)

 @commands.command()
 async def dice(self, ctx):
        botdice =["sbdice 1","sbdice 2","sbdice 3","sbdice 4","sbdice 5","sbdice 6"]
        botdi = random.choice(botdice)
        if ctx.message.content == botdi:
            await ctx.send("You were right! :partying_face: ")
        else:
            await ctx.send("you were wrong. :pensive:")
 @commands.command()
 async def joke(self, ctx):
        await ctx.send("Why did the chicken cross the road? It was getting to the idiot's house.")
        time.sleep(5)
        await ctx.send("Knock knock.")
        time.sleep(3)
        await ctx.send("It's the chicken.")
 @commands.command()
 async def jojoke(self, ctx):
     await ctx.send("You expected a jojoke, but it was me, DIO!")
     await ctx.send("https://cdn.discordapp.com/attachments/559455534965850142/648223929613418526/Z.png")
     time.sleep(2)
     await ctx.send("shit that's a jojoke")
 @commands.command()
 async def facts(self, ctx):
    await ctx.send("https://imgur.com/a/H63R8hG")
 @commands.command()
 async def coinflip(self, ctx):
        coin = ["Heads", "Tails"]
        coinf = random.choice(coin)
        await ctx.send(coinf)
 @commands.command()
 async def story(self, ctx):
        await ctx.send("I see you would like a story. Now preparing...")
        await ctx.send (f"You are {ctx.message.author}, correct?")
        if 'yes' or 'YES' in message.content:
         await ctx.send (f"Okay then, {ctx.message.author} The great legend of {ctx.message.author} is about to begin!")
         embed = discord.Embed(name=f"The story of {ctx.message.author}", description="By DripBot")
         embed.add_field("Don't like the story? Add a suggestion!")
         await ctx.send(embed)
 @commands.command()
 async def dance(self, ctx):
    await ctx.send("https://tenor.com/view/dancing-coffin-coffin-dance-funeral-funny-farewell-gif-16737844")
 @commands.command()
 async def dab(self, ctx):
    await ctx.send("You asked.")
    time.sleep(1)
    await ctx.send("https://cdn.discordapp.com/attachments/385837258768515083/645685851698888704/165ouZ0gVczfHuvwCma1S96R7I0wAAAABJRU5ErkJggg.png")
 @commands.command()
 async def randmeme(self, ctx):
        meme = ["https://cdn.discordapp.com/attachments/645695800352964618/646018286504509440/ae6f07ce-085e-11ea-8da7-95ed4a38ab68.png","https://cdn.discordapp.com/attachments/645695800352964618/646018152743829514/EU-internet-meme_trans_NvBQzQNjv4BqpJliwavx4coWFCaEkEsb3pVDAZXwknrCGX2X3jMDFdw.png","https://cdn.discordapp.com/attachments/645695800352964618/646018080878624788/label-face-crowd-text-homedecor-person-human.png","https://cdn.discordapp.com/attachments/645695800352964618/646017964226904094/e0uhelxpmkm31.png", "https://i.redd.it/rwfpxonc0nz31.jpg", "https://preview.redd.it/vr89p4mf5nz31.jpg?width=640&crop=smart&auto=webp&s=98f4ec3d7e5a4c7b80c8178b5a714883cab795ad", "https://preview.redd.it/lbaosswd2oz31.jpg?width=640&crop=smart&auto=webp&s=7c5e4b6f2dcbadc7c48b0fe0078b327b40a95745", "https://preview.redd.it/bizn2l9qanz31.jpg?width=640&crop=smart&auto=webp&s=cc68cf8eb224ee6a58495e96be074b1ad844ea04", "https://preview.redd.it/bhf5et6y6oz31.jpg?width=640&crop=smart&auto=webp&s=8c03dd198478a09d1627afad3d47084153962eeb", "https://preview.redd.it/tmdhramd0nz31.jpg?width=640&crop=smart&auto=webp&s=52a4c5b04a115a478b9441d2b0a8b27cc33575c9", "https://preview.redd.it/66b0rfktlmz31.jpg?width=640&crop=smart&auto=webp&s=9893a79032204593c1177435117c8ea27ff70dcd", "https://preview.redd.it/jn7060kmwnz31.jpg?width=640&crop=smart&auto=webp&s=e66d4ccbd3b2985af35d94397ea8b1b7287e0369", "https://preview.redd.it/4j0bknoj4nz31.jpg?width=640&crop=smart&auto=webp&s=ce9de25e30f3bbdbfe2e73f2827e00ded833a055", "https://preview.redd.it/kax0nm6ycnz31.jpg?width=640&crop=smart&auto=webp&s=002c64f8d8d98dfdba74c58188abaa697fb9581d", "https://preview.redd.it/lckm8ryw9nz31.jpg?width=640&crop=smart&auto=webp&s=3a3e55fb01bd8e376a5023a1487dd105b29308b7", "https://preview.redd.it/s786dtyhsnz31.jpg?width=640&crop=smart&auto=webp&s=cf22f41f0aac182a98288abc5ce2a27fb87ece67", "https://preview.redd.it/frai7o57knz31.jpg?width=640&crop=smart&auto=webp&s=aa669a7ce9d75bf1f7799d88a3cc2fa8de19b35f", "https://preview.redd.it/qn5uczwbcnz31.jpg?width=640&crop=smart&auto=webp&s=fb0b9c3cee2280b37ac703bf54819cf05d064839", "https://i.redd.it/xbs7mcla8oz31.png", "https://external-preview.redd.it/56hO7MTgDT4zxmAxycINZ319yWXbfbpc6uBkmYQ12Aw.jpg?width=640&crop=smart&auto=webp&s=d07e4004c7f35b485ffaab67f93270adfa5dab11", "https://preview.redd.it/47xuwt4vcmz31.jpg?width=640&crop=smart&auto=webp&s=426d95aeb070dc6ece565301a0b22cb74696a5e8"]
        memes = random.choice(meme)
        await ctx.send(memes)
 @commands.command()
 async def drift(self, ctx):
        await ctx.send("...k..kansei dorifto!?!?")
        await ctx.send("https://gfycat.com/zigzagbasicblackpanther")
def setup(bot):
    bot.add_cog(FunCog(bot))
