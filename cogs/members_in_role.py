import nextcord
from nextcord.ext import commands

class listroleusers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def inrole(self, ctx, *, role: nextcord.Role):
      embed = nextcord.Embed(title=f'In role {role}', color=0xFF6D7A)
      member_list = ("\n".join(str(member) for member in role.members))
      embed.add_field(name='Members:', value=f'{member_list}')
      await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(listroleusers(bot))
