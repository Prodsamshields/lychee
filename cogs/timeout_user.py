import nextcord
from nextcord.ext import commands
import os
from datetime import datetime
import humanfriendly
from datetime import timedelta


class timed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: nextcord.Member=None, time=None, *, reason=None):
        if member.bot:
            await ctx.send('Leave the robots out of this!')
            return
          
        elif member.guild_permissions.administrator or member.guild_permissions.moderate_members:
            await ctx.send(f'I can\'t time that person out. They are a mod/ admin.')
            return
      
        time = humanfriendly.parse_timespan(time)
        embed = nextcord.Embed(title=None, description=f'You have been timed out in {ctx.guild} for {time} minutes for reason: {reason}', color=0xFF6D7A, timestamp=ctx.message.created_at)
        await member.timeout(nextcord.utils.utcnow() + timedelta(minutes=time), reason=reason)
        
        channel = await member.create_dm()  
        await channel.send(embed=embed)
        
        await ctx.channel.purge(limit=1)
        embed = nextcord.Embed(description=f'{member} has been timed out for {time} minutes for reason: {reason}', color=0xFF6D7A)
        await ctx.channel.send(embed=embed)



def setup(bot):
    bot.add_cog(timed(bot))
