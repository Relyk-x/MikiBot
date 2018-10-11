# Initialise
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

# Member Join
Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, "Hey there I'm Sector Bot")
    print('Sent message to ' + member.name)

# Start Up
@client.event
async def on_ready():
   await client.change_presence(game=discord.Game(name="over the server",url="https://www.twitch.tv/streamer",type=3))
   print('Sector bot is up and running...')

# Greetings
@client.event
async def on_message(message):
    if message.content == 'hello' or message.content == 'Hello' or message.content == 'hello?' or message.content == 'Hello?' or message.content == 'hey' or message.content == 'Hey':
            await client.send_message(message.channel,'Hey there buddy!')

# Translate
    if message.content:
#YES
        if message.content == 'yes' or message.content == 'Yes' or message.content == 'Yea' or message.content == 'yea' or message.content == 'Yeah' or message.content == 'yeah' or message.content == 'yep' or message.content == 'Yep' or message.content == 'Ye' or message.content == 'ye':
            em = discord.Embed(title= '<:translate:498838802064867329> Sector Translate:', description= 'English: Yes | Latin: Etiam', color=0xffffff,)
            await client.send_message(message.channel, embed=em)
#NO
        elif message.content == 'no' or message.content == 'No' or message.content == 'nope' or message.content == 'nah' or message.content == 'Nah' or message.content == 'Nope':
            em = discord.Embed(title= '<:translate:498838802064867329> Sector Translate:', description= 'English: No | Latin: Nihil', color=0xffffff,)
            await client.send_message(message.channel, embed=em)
#WHAT
        elif message.content == 'What?' or message.content == 'what?' or message.content == 'What' or message.content == 'what' or message.content == 'Wha' or message.content == 'wha' or message.content == 'Wha?' or message.content == 'wha?':
            em = discord.Embed(title= '<:translate:498838802064867329> Sector Translate:', description= 'English: What? | Latin: Quid est?', color=0xffffff,)
            await client.send_message(message.channel, embed=em)

# Memes
    if message.content.startswith('-meme'):
        randomlist = ['https://goo.gl/dwJD8o',  #Batman
                      'https://goo.gl/1wezZw',  #Dr. Phill
                      'https://goo.gl/nB6oCw',  #Gandalf
                      'https://goo.gl/viStSC',  #Zach Galifianakis
                      'https://goo.gl/U3pEhp',  #Chuck Norris
                      'https://goo.gl/YZSPxx',  #Fat Controller
                      'https://goo.gl/n2Hajn',  #Ocean
                      'https://goo.gl/CDwmTj',  #Austin Powers
                      'https://goo.gl/pjkwqZ',  #Nemo
                      'https://goo.gl/79AANm',  #Knights
                      'https://goo.gl/AxaSrv',  #Carl, Wheels
                      'https://goo.gl/WB1PTd',  #Carl, Vader
                      'https://goo.gl/Kx7auW',  #Carl, Pew
        em = discord.Embed(title= 'Meme:',  color=0xffffff,)
        em.set_image(url='%s' %(random.choice(randomlist),))
        await client.send_message(message.channel, embed=em)
        
# Games
# DICE ROLL
    if message.content.startswith('-diceroll') or message.content.startswith('-dr'):
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title= '<:die:498871525450186753> Game: Dice Roll',  color=0xffffff, description= 'You rolled a %s' %(random.choice(randomlist),))
        em.add_field(name='`Other Games:`', value='Coin flip | -coinflip/-cf', inline=True)
        await client.send_message(message.channel, embed=em)
# COIN FLIP
    elif message.content.startswith('-coinflip') or message.content.startswith('-cf'):
        randomlist = ['heads','tails',]
        em = discord.Embed(title= '<:token:498835395270803466> Game: Coin Flip',  color=0xffffff, description= 'You flipped %s' %(random.choice(randomlist),))
        em.add_field(name='`Other Games:`', value='Dice Roll | -diceroll/-dr', inline=True)
        await client.send_message(message.channel, embed=em)

#Bot Token
client.run(BOT_TOKEN)
