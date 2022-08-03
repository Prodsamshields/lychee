import nextcord
from nextcord.ext import commands
import json


class onguildjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        role = nextcord.utils.get(guild.roles, name="lychee verified")
        if role:
            pass
        else:
            await guild.create_role(name="lychee verified")
        with open("./prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = ","
        with open("./prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
    
        with open("./welcome_msgs.json", "r") as f:
            welcome_msgs = json.load(f)
        welcome_msgs[str(guild.id)] = "Welcome to the server! Take a look at the rules to begin! "
        with open("./welcome_msgs.json", "w") as f:
            json.dump(welcome_msgs, f, indent=4)
    
        channel = guild.system_channel
        
        embed = nextcord.Embed(title="Welcome to lychee", description="Thanks for adding lychee to your server! If you need help with any of lychee\"s commands, please use the \"help\" command")
        embed.add_field(name="Welcome messages", value="By default, I send this message when a new user joins the server: \"Welcome to the server! Take a look at the rules to begin! (user mention)\" \nTo change this, use the \"setwelcome\" command.", inline=False)
        embed.add_field(name="Our website", value="[lychee.gg](https://dev--lychee-xyz.prodsamshields.autocode.gg/)", inline=True)
        embed.add_field(name="Support server", value="[server link](https://discord.gg/TEU43brVRe)", inline=True)
        
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(onguildjoin(bot))
