import nextcord
from nextcord.ext import commands
import json

class help_cmd_custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.purge(limit=1)
        with open("./prefixes.json", "r") as f:
            prefix = json.load(f)
        with open("./welcome_msgs.json", "r") as f:
            welcome = json.load(f)
        prefix1 = prefix[str(ctx.guild.id)]
        welcome1 = welcome[str(ctx.guild.id)]
        channel = await ctx.author.create_dm()
        embed = nextcord.Embed(title=f"Help | {ctx.guild}", description=f'The bot prefix for this server is: {prefix1} \nCurrent welcome message is: \'{welcome1}\'', color=0xFF6D7A)
        embed.add_field(name="Lychee official website", value="[lychee.gg](https://dev--lychee-xyz.prodsamshields.autocode.gg/)")
        embed.add_field(name='List of commands', value="[commands](https://dev--lychee-xyz.prodsamshields.autocode.gg/Commands.html)")
        embed.add_field(name="Support/ home server", value="[server link](https://discord.gg/TEU43brVRe)")
        try:
          await channel.send(embed=embed)
        except nextcord.DiscordException:
          await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help_cmd_custom(bot))
