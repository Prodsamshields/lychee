import nextcord
from nextcord.ext import commands
import os
import json

class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot   

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setwelcome(self, ctx, *, welcome):
        with open('./prefixes.json', 'r') as f:
            welcome_msg = json.load(f)
        
        welcome_msg[str(ctx.guild.id)] = welcome
    
        try:
            with open('./welcome_msgs.json', 'w') as f:
                json.dump(welcome_msg, f, indent=4)
            embed = nextcord.Embed(description=f'Welcome message successfully set to: \'{welcome}\'', color=0xFF6D7A)
            await ctx.channel.send(embed=embed)
        except:
            return


def setup(bot):
    bot.add_cog(welcome(bot))
