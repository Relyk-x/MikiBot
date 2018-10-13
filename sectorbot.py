# Initialise
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random
from discord import Game
from itertools import cycle

Client = discord.client
client = commands.Bot(command_prefix = 's/')
Clientdiscord = discord.Client()

servers = list(client.servers)
status = ['for s/help', 'for bot suggestions']
# WATCHING 'over ' + str(len(client.servers)) + ' servers'

async def change_status():
  await client.wait_until_ready()
  msgs = cycle(status)

  while not client.is_closed:
     current_status = next(msgs)
     await client.change_presence(game=discord.Game(name=current_status, url="https://www.twitch.tv/streamer",type=3))
     await asyncio.sleep(10)
      
# Start Up
@client.event
async def on_member_join(member):
    print('Sent message to ' + member.name)
    servers = list(client.servers)
    print("Connected on " + str(len(client.servers)) + "servers:")
    for x in range(len(servers)):
     print(' ' + servers[x-1].name)
    await client.send_message(member, "Hey there I'm Sector Bot")
    print('Sent message to ' + member.name)
async def on_ready():
   print('Sector Bot is up and running with ' + str(len(client.servers)) + ' servers connected!')
   print('Sector bot is up and running...')

# Multiple Commands
@client.event
async def on_message(message):
    # Memes
    if message.content.startswith('s/meme'):
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
                      'https://goo.gl/N9m7kF',  #Slut
                      'https://goo.gl/UFNkSe',  #Shaggy, Weed
                    ]
        em = discord.Embed(title= 'Meme:',  color=0xffffff,)
        em.set_image(url='%s' %(random.choice(randomlist),))
        await client.send_message(message.channel, embed=em)
    # Password Generator
    if message.content == 's/password':
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
    # There are about 23,535,820 different password combinations that can be generated.
        encryptedpass = (key1 + key2 + key3 + key4 + key5 + key6 + key7 + key8)
        await client.send_message(message.author,'Here is your randomly generated password: ' + encryptedpass)
        f = open('authpass.txt','a')
        f.write('\n' + 'Password: ' + encryptedpass + ' was generated by ' + str(message.author))
        f.close()
    # Hello
    if message.content == 's/greet':
        em = discord.Embed(description='Hey there buddy! :wave:', color=0xffffff)
        await client.send_message(message.channel, embed=em)
    # Vote
    if message.content == 's/vote':
        em = discord.Embed(description='You can vote here: https://discordbots.org/bot/496214977267630080/vote', color=0xffffff)
        await client.send_message(message.channel, embed=em)
    # Dice Roll
    if message.content.startswith('s/diceroll') or message.content.startswith('s/dr'):
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title = '<:die:500434709835153408> **Dice Roll**', color=0xffffff, description="You rolled the number... %s \n\n <:discord:500467821034078218> If you'd like to invite Sector Bot to your own server go to: \n https://goo.gl/2rp6n2" %(random.choice(randomlist),))
        em.set_author(name='Game:')
        await client.send_message(message.channel, embed=em)
    # Coin Flip
    elif message.content.startswith('s/coinflip') or message.content.startswith('s/cf'):
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title = '<:token:500434456734203904> **Coin Flip**', color=0xffffff, description="You flipped... %s \n\n <:discord:500467821034078218> If you'd like to invite Sector Bot to your own server go to: \n https://goo.gl/2rp6n2" %(random.choice(randomlist),))
        em.set_author(name='Game:')
        await client.send_message(message.channel, embed=em)
    # Help
    if ('s/help') in message.content:
        em = discord.Embed(title="Discord Server", description="For any other help please join our Discord server...", url="https://discord.gg/eRHsyFg", color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        em.add_field(name="Commands:", value="s/<command>", inline=False)
        em.add_field(name="s/greet", value="Sends a greeting in the channel.", inline=False)
        em.add_field(name="s/vote", value="Vote for this bot.", inline=False)
        em.add_field(name="s/meme", value="Sends a random meme from Sector Bot’s stash.", inline=False)
        em.add_field(name="s/password", value="Generates a random password.", inline=False)
        em.add_field(name="s/diceroll", value="Rolls a six sided die.", inline=False)
        em.add_field(name="s/coinflip", value="Flips a coin, could be heads could be tails.", inline=False)
        await client.send_message(message.channel, embed=em)

#Bot Token
client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))
