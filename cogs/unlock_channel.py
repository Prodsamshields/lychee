import nextcord
from nextcord.ext import commands

class removelockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : nextcord.TextChannel=None, reason=None):
        emoji = '🔓'
        
        if channel is None:
            channel_nums = len(ctx.guild.text_channels)
            embed2 = nextcord.Embed(description=f'{emoji} {channel_nums}/{channel_nums} channels have been unlocked.', color=0xFF6D7A)
            for channel in ctx.guild.text_channels:
                unlock_channel = channel
                overwrite = unlock_channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = True
                await unlock_channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(embed=embed2)
        
        else:
            try:
                embed1 = nextcord.Embed(description=f'{emoji} {channel.mention} unlocked for reason: {reason}', color=0xFF6D7A) 
                channel = channel or ctx.channel
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = True
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                await ctx.send(embed=embed1)
            except nextcord.DiscordException:
                return



def setup(bot):
    bot.add_cog(removelockdown(bot))
