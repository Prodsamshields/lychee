from nextcord.ext import commands
import json

class welcomecheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def welcome(self, ctx):
      with open("./welcome_msgs.json", "r") as f:
        welcome_msg = json.load(f)
      welcome = welcome_msg[str(ctx.guild.id)]
      await ctx.send(f"Current welcome message for {ctx.guild} is: \"{welcome}\"")



def setup(bot):
    bot.add_cog(welcomecheck(bot))
