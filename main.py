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

captcha1 = your captcha
captcha2 = your captcha
etc...

@client.command(pass_context = True)
async def verify(ctx):
  role = nextcord.utils.get(ctx.guild.roles, name="lychee verified")
  if role in ctx.author.roles:
    await ctx.send('You are already verified.')
    return
  await ctx.channel.purge(limit=1)
  channel = await ctx.author.create_dm()
  def check(m):
      return m.author == ctx.author and m.channel == channel
  captcha_images = (captcha1, captcha2, captcha3, etc...)
  image_random = random.choice(captcha_images)
  answer = ("captcha answer", "captcha answer", "captcha answer", "captcha answer", "captcha answer", etc...)
  embed = nextcord.Embed(title='Captcha Challenge | lychee', color=0xFF6D7A)
  try:
    embed.set_image(url=image_random)
  except:
    pass
  embed.add_field(name='Type what you see below', value=f'You have 3 attempts \nFor each attempt, you will have 1 minute to respond. \nIf you fail the captcha challenge, you will be kicked from server \'{ctx.guild}\'. However, you can rejoin and try again.')
  role = nextcord.utils.get(ctx.guild.roles, name="lychee verified")
  if role:
    pass
  else:
    try:
      await ctx.guild.create_role(name='lychee verified')
      role = nextcord.utils.get(ctx.guild.roles, name="lychee verified")
      await ctx.author.add_roles(role)
    except:
      return
  await channel.send(embed=embed)
  try:
    for i in range(0, 3):
      guess = await client.wait_for('message', check=check, timeout=60)
      # it will stop listening for messages after 60 seconds
      if guess.content in answer:
          await channel.send(f'Captcha challenge complete! You are now verified in {ctx.guild}')
          await ctx.author.add_roles(role)           
          return
        
      else:
          await channel.send("Incorrect answer.")

    else:
        await channel.send("You have failed the captcha challenge. If you wish to retry, join again and rerun the verify command.")
        await ctx.author.kick()

  except:
    return
 
client.run(your token here)
