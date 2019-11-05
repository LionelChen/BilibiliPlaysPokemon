import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description=description)
balance = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

class MyClient(discord.Client):

    balance = {}

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author == client.user:
            return

        if message.content.startswith('$add'):
            msg = message.content.split()
            usr_id = msg[1]
            await message.channel.send(msg)

    async def kick(self):
        print('Logged on as {0}!'.format(self.user))



bot.run('NjQxMzAyMTQxODc2NTY4MDY0.XcGZ9A.AsL26saUlsIMzKbdksHLXK8WrKc')