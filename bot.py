import os
import random

from discord.ext import commands

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('BOT_PREFIX')

bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Bonjourno {member.name}, welcome to the server.'
    )


@bot.command(name='rip', help='Responds with a random quote')
async def rip_reply(ctx):
    funny_messages = [
        'WAAH!',
        'Press F boys',
        'get bent',
        'sit, kid',
        'Nothing personal, kid',
        'ye',
        'RRRREEEEEEE',
        'Mom said its my turn on the xbox',
        'Knees weak,\nArm\'sa heavy,\nMom\'s spaghetti',
        'I don\'t feel so good Mr. Stark',
        'BOOM HEADSHOT!'
    ]

    response = random.choice(funny_messages)
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role to use this command.')


@bot.command(name='create-channel')
@commands.has_role('Mr. World Wide')
async def create_channel(ctx, channel_name=''):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Created a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


bot.run(TOKEN)
