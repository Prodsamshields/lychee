import nextcord
from nextcord.ext import commands


class slowmotion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def slowmode(self, ctx, seconds=None):
      if seconds:
        if seconds == int:
          if int(seconds) > 21600:
            embed = nextcord.Embed(description=f'Slowmode cannot exceed 21,600 seconds.', color=0xFF6D7A)
            await ctx.send(embed=embed)
          elif int(seconds) < 21600:
              await ctx.channel.edit(slowmode_delay=int(seconds))
              embed = nextcord.Embed(description=f'Slowmode set to {int(seconds)} seconds in {ctx.channel.mention}', color=0xFF6D7A)
              await ctx.send(embed=embed)
          else:
              embed = nextcord.Embed(description=f'Error in command request. Please try again.', color=0xFF6D7A)
              await ctx.send(embed=embed)
              return
        else:
          if seconds == 'none':
              for channel in ctx.guild.text_channels:
                  await channel.edit(slowmode_delay=0)
              embed = nextcord.Embed(description=f'Slowmode removed from all channels.', color=0xFF6D7A)
              await ctx.send(embed=embed)
          elif seconds == 'all':
              for channel in ctx.guild.text_channels:
                  await channel.edit(slowmode_delay=60)
              embed = nextcord.Embed(description=f'60 second slowmode added to all channels.', color=0xFF6D7A)
              await ctx.send(embed=embed)
      else:
        await ctx.channel.edit(slowmode_delay=0)
        embed = nextcord.Embed(description=f'Slowmode removed from {ctx.channel.mention}', color=0xFF6D7A)
        await ctx.send(embed=embed)
        return



def setup(bot):
    bot.add_cog(slowmotion(bot))
