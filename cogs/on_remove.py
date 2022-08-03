from nextcord.ext import commands
import json


class onguildremove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open("./prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes.pop(str(guild.id))
        with open("./prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
    
        with open("./welcome_msgs.json", "r") as f:
            welcome_msgs = json.load(f)
        welcome_msgs.pop[str(guild.id)]
        with open("./welcome_msgs.json", "w") as f:
            json.dump(welcome_msgs, f, indent=4)

def setup(bot):
    bot.add_cog(onguildremove(bot))
