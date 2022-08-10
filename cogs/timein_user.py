import nextcord
from nextcord.ext import commands

class timedin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_permissions(moderate_members=True)
    async def timein(self, ctx, member: nextcord.Member=None, *, reason=None):
        embed = nextcord.Embed(title=None, description=f'You have removed from timeout in {ctx.guild} for reason: {reason}', color=0xFF6D7A, timestamp=ctx.message.created_at)
        
        await member.timeout(None, reason=reason)
        channel = await member.create_dm()
        await channel.send(embed=embed)
        
        await ctx.channel.purge(limit=1)
        embed = nextcord.Embed(description=f'{member} has been timed in for reason: {reason}', color=0xFF6D7A)
        await ctx.channel.send(embed=embed)



def setup(bot):
    bot.add_cog(timedin(bot))
