import nextcord
from nextcord.ext import commands
import os
import json

class prefixset(commands.Cog, name="sets the bot prefix"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        with open('./prefixes.json', 'r') as f:
            prefixes = json.load(f)
        
        prefixes[str(ctx.guild.id)] = prefix
        try:
            with open('./prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
            embed = nextcord.Embed(description=f'Prefix successfully changed to {prefix}', color=0xFF6D7A)
            await ctx.channel.send(embed=embed)
        except:
            return

def setup(bot):
    bot.add_cog(prefixset(bot))
