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
        'BOOM HEADSHOT!',
        'DAMN, WHATSA MATHEMATICS, WHATSA MATHEMATICS',
        'My name is Inigo Montoya. You killed my father. Prepare to die.',
        'My name is Yoshikage Kira. I\'m 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don\'t smoke, but I occasionally drink. I\'m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn\'t lose to anyone.',
        'Hayato.',
        'Oh? You\'re approaching me?',
        'Scoops. Scoops Hagendaz.',
        'OH HE DA MANGO SENTINEL!',
        'MAHVEL BABAY!\nOOH\nOOH\nOOH\nOOH\nHE THINKIN NEW YORK KNICKS',
        'LEEEEEEROOOOOOOOOY JEEEEENKINSS',
        '2 + 2 = 5 quikmafs',
        'Samoa Joe KNOWS he doesn\'t want any of this',
        'oof'
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
