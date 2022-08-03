import nextcord
from nextcord.ext import commands
import os


class purgemsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def purge(self, ctx, amount=2):
      await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(purgemsg(bot))
