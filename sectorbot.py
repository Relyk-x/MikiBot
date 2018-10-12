# Initialise
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
from itertools import cycle
import os

# Member Join
Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()

@client.event
async def on_member_join(member):
    await client.change_presence(game=discord.Game(name='over ' + str(len(client.servers)) + ' servers', url="https://www.twitch.tv/streamer",type=3))
    print('Sent message to ' + member.name)
    servers = list(client.servers)
    print("Connected on " + str(len(client.servers)) + "servers:")
    for x in range(len(servers)):
     print(' ' + servers[x-1].name)

async def on_ready():
    await client.change_presence(game=discord.Game(name='over ' + str(len(client.servers)) + ' servers', url="https://www.twitch.tv/streamer",type=3))
    print('Sector bot is up and running...')

# Greetings
@client.event
async def on_message(message):
    if message.content.lower() == 'hello' or message.content == 'hello?' or message.content == 'hey':
        await client.send_message(message.channel,'Hey there buddy!')

# Translate
    if message.content:
#YES
        if message.content == 'yes' or message.content == 'yea' or message.content == 'yeah' or message.content == 'yep' or message.content == 'ye':
            em = discord.Embed(title= '<:translate:498838802064867329> Sector Translate:', description= 'English: Yes | Latin: Etiam', color=0xffffff,)
            await client.send_message(message.channel, embed=em)
#NO
        elif message.content == 'no' or message.content == 'nope' or message.content == 'nah':
            em = discord.Embed(title= '<:translate:498838802064867329> Sector Translate:', description= 'English: No | Latin: Nihil', color=0xffffff,)
            await client.send_message(message.channel, embed=em)
#WHAT
        elif message.content == 'what?' or message.content == 'what' or message.content == 'wha' or message.content == 'wha?':
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
                      ]
        em = discord.Embed(title= 'Meme:',  color=0xffffff,)
        em.set_image(url='%s' %(random.choice(randomlist),))
        await client.send_message(message.channel, embed=em)

#password generator
if message.content == '-randompassword':
      encryptkey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
      encryptcode = ['1','2','3','4','5','6','7','8','9',]
      count1 = random.randint(1, 26)
      count2 = random.randint(1, 26)
      count3 = random.randint(1, 26)
      count4 = random.randint(1, 26)
      count5 = random.randint(1, 26)
      count6 = random.randint(1, 26)
      count7 = random.randint(1, 26)
      count8 = random.randint(1, 26)
      if count1 < 13:
        key1 = (random.choice(encryptkey))
      if count1 >= 13: 
        key1 = (random.choice(encryptcode))
      if count2 < 13:
        key2 = (random.choice(encryptkey))
      if count2 >= 13: 
        key2 = (random.choice(encryptcode))
      if count3 < 13:
        key3 = (random.choice(encryptkey))
      if count3 >= 13: 
        key3 = (random.choice(encryptcode))
      if count4 < 13:
        key4 = (random.choice(encryptkey))
      if count4 >= 13: 
        key4 = (random.choice(encryptcode))
      if count5 < 13:
        key5 = (random.choice(encryptkey))
      if count5 >= 13: 
        key5 = (random.choice(encryptcode))
      if count6 < 13:
        key6 = (random.choice(encryptkey))
      if count6 >= 13: 
        key6 = (random.choice(encryptcode))
      if count7 < 13:
        key7 = (random.choice(encryptkey))
      if count7 >= 13: 
        key7 = (random.choice(encryptcode))
      if count8 < 13:
       key8 = (random.choice(encryptkey))
      if count8 >= 13: 
        key8 = (random.choice(encryptcode))
# There are about 23535820 different password combinations that can be generated.
      encryptedpass = (key1 + key2 + key3 + key4 + key5 + key6 + key7 + key8)
      await client.send_message(message.channel,'Here is your random generated password : ' + encryptedpass)
      f = open('authpass.txt','a')
      f.write('\n' + 'Password: ' + encryptedpass + ' was generated by ' + str(message.author))
      f.close()

# Games
# DICE ROLL
    if message.content.startswith('-diceroll') or message.content.startswith('-dr'):
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title= 'Game: Dice Roll',  color=0xffffff, description= '<:die:498871525450186753> You rolled a %s' %(random.choice(randomlist),))
        em.add_field(name='`Other Games:`', value='Coin flip | -coinflip/-cf \nTic Tac Toe | `COMING SOON`', inline=True)
        await client.send_message(message.channel, embed=em)
# COIN FLIP
    elif message.content.startswith('-coinflip') or message.content.startswith('-cf'):
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title= 'Game: Coin Flip',  color=0xffffff, description= '<:token:498835395270803466> You flipped %s' %(random.choice(randomlist),))
        em.add_field(name='`Other Games:`', value='Dice Roll | -diceroll/-dr \nTic Tac Toe | `COMING SOON`', inline=True)
        await client.send_message(message.channel, embed=em)
# TICTACTOE
        # COMING SOON

#Bot Token
client.run(os.getenv('BOT_TOKEN'))
