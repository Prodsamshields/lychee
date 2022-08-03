import nextcord
from nextcord.ext import commands
import os


class lockitdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : nextcord.TextChannel=None, reason=None):
        emoji = '🔒'
        if channel is None:
            channel_nums = len(ctx.guild.text_channels)
            embed2 = nextcord.Embed(description=f'{emoji} {channel_nums}/{channel_nums} channels have been locked.', color=0xFF6D7A)
            for channel in ctx.guild.text_channels:
                lock_channel = channel
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = False
                await lock_channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(embed=embed2)
        elif channel and channel != None:
            try:
                embed1 = nextcord.Embed(description=f'{emoji} {channel.mention} locked for reason: {reason}', color=0xFF6D7A) 
                channel = channel or ctx.channel
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = False
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                await ctx.send(embed=embed1)
            except nextcord.DiscordException:
                return
        else:
            return


def setup(bot):
    bot.add_cog(lockitdown(bot))
