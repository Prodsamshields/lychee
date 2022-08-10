import nextcord
from nextcord.ext import commands
import os
import json
import time
import random

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True


def get_prefix(client, message):
    if not message.guild:
        return ","

    try:
        with open("./prefixes.json", "r") as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

    except nextcord.DiscordException:
        return ","

client = commands.Bot(command_prefix=get_prefix, intents=intents, activity = nextcord.Game(name="| ,help"), help_command=None)

if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
    print('all cogs loaded')


def get_welcome(client, message):
    if not message.guild:
        return "Welcome to the server! Take a look at the rules to begin! "

    try:
        with open("./prefixes.json", "r") as f:
            welcome_message = json.load(f)

        return welcome_message[str(message.guild.id)]

    except nextcord.DiscordException:
        return "Welcome to the server! Take a look at the rules to begin! "

@client.event
async def on_ready():
    print("lychee is started and online")

@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)
    pass

client.run(your token here)
