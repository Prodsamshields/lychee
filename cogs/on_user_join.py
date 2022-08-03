import nextcord
from nextcord.ext import commands
import time
from datetime import datetime
import json

class onusrjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
          return
        channel1 = member.guild.system_channel
        
        if time.time() - member.created_at.timestamp() < 172800:
            channel = await member.create_dm()
            embed = nextcord.Embed(title="lychee - please come back later", description=f"I noticed that your account was created less than 2 days ago. Unfortunately that means you are unable to join {member.guild} at this time. \nFeel free to join back when your account is older than 2 days!", color=0xFF6D7A, timestamp=datetime.utcnow())
            await channel.send(embed=embed)
            await member.kick()
            
        if channel1 is not None:
            with open("./welcome_msgs.json", "r") as f:
                welcome_msgs = json.load(f)
                welcome = welcome_msgs[str(member.guild.id)]
            await channel1.send(f"{welcome} " + member.mention)
            
        else:
            return


def setup(bot):
    bot.add_cog(onusrjoin(bot))
