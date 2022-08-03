import nextcord
from nextcord.ext import commands

class banned(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason='None'):  
        if member.bot:
            await ctx.send('Leave the robots out of this!')
            return
        elif member.guild_permissions.administrator or member.guild_permissions.moderator:
            await ctx.send(f'I can\'t ban that person. They are a mod/ admin.')
            return
        embed = nextcord.Embed(title='lychee', description=f'You have been banned from {ctx.guild} for reason: {reason}', color=0xFF6D7A, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"ID: {ctx.message.id}")
        channel = await member.create_dm()
        await channel.send(embed=embed)
        embed = nextcord.Embed(description=f'{member} has been banned for reason: {reason}', color=0xFF6D7A, timestamp=ctx.message.created_at)
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(banned(bot))
