import nextcord
from nextcord.ext import commands
import os


class unbanned(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def unban(self, ctx, *, member):
        embed = nextcord.Embed(description=f'{member} has been unbanned', color=0xFF6D7A, timestamp=ctx.message.created_at)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        
        for ban_entry in banned_users:
            user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(embed=embed)
            return
        
        else:
            await ctx.send(f'failed to unban member {member} please try again')

def setup(bot):
    bot.add_cog(unbanned(bot))
