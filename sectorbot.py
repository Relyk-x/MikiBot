# Initialise
import discord
from discord.ext import commands
import asyncio
import time
import os
import random
from discord import Game
from itertools import cycle

Client = discord.client
client = commands.Bot(command_prefix = ';')
Clientdiscord = discord.Client()

# Setting Bot status 'Watching'
async def change_status():
  await client.wait_until_ready()
  status = ['for: ;help | v0.2.3', 'for: bot suggestions', 'for: @Relyk-x#2896']
# WATCHING 'over ' + str(len(bot.servers)) + ' servers' ## v0.2.3,8##
  msgs = cycle(status)

  while not client.is_closed:
     current_status = next(msgs)
     await client.change_presence(game=discord.Game(name=current_status, url="https://www.twitch.tv/streamer",type=3))
     await asyncio.sleep(10)
      
# Start Up
@client.event
async def on_member_join(member):
    servers = list(client.servers)
    print("Connected on " + str(len(bot.servers)) + " servers:")
    for x in range(len(servers)):
     print(' ' + servers[x-1].name)
    await client.send_message(member, "Hey there I'm Sector Bot")
    
# Checking if bot is online    
async def on_ready():
   print('Sector Bot is up and running with ' + str(len(client.servers)) + ' servers connected!')

# Multiple Commands
@client.event
async def on_message(message):
    
    # Purge
    if message.content.startswith(';purge ') and not message.content[7:]=='':
        message_amount = int(message.content[7:])
        deleted = await client.purge_from(message.channel, limit=message_amount, check=on_message)
        em = discord.Embed(description='Purged {} message(s) from this channel ⚠'.format(len(deleted)), color=0xe9b820,)
        selfdel = await client.send_message(message.channel, embed=em)
        await asyncio.sleep(10)
        await client.delete_message(selfdel)
        
    # Say
    content = message.content
    if content.startswith(';say '):
        await client.send_message(message.channel, content[5:])
        await client.delete_message(message)
        
    # Memes
    if (';meme') in message.content:
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
        em = discord.Embed(title= 'Meme:', color=0xe9b820,)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
        
    # Password Generator
    if (';password') in message.content:
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
        em = discord.Embed(description='Here is your randomly generated password: ' + '`' + encryptedpass + '`', color=0xe9b820)
        await client.send_message(message.author, embed=em)
        f = open('authpass.txt','a')
        f.write('\n' + 'Password: ' + encryptedpass + ' was generated by ' + str(message.author))
        f.close()
        
    # Invite
    if (';invite') in message.content:
        em = discord.Embed(description="If you'd like to add Sector Bot to your server, Click here: https://goo.gl/2rp6n2", color=0xe9b820)
        await client.send_message(message.channel, embed=em)
        
    # Server Count
    if (';servercount') in message.content:
        em = discord.Embed(description='Currently watching over ' + str(len(client.servers)) + 'Discord servers <:discordp:500719998172659713>', color=0xe9b820)
        await client.send_message(message.channel, embed=em)
        
    # Hello
    if (';greet') in message.content:
        em = discord.Embed(description='Hey there buddy! :wave:', color=0xe9b820)
        await client.send_message(message.channel, embed=em)
        
    # Vote
    if (';vote') in message.content:
        em = discord.Embed(description='You can vote here: https://discordbots.org/bot/496214977267630080/vote', color=0xe9b820)
        await client.send_message(message.channel, embed=em)
        
##### Version
    if (';version') in message.content:
        em = discord.Embed(description='The current version of Sector Bot is: `v0.2.3`', color=0xe9b820)
        await client.send_message(message.channel, embed=em)
    
    # Dice Roll
    if (';diceroll') in message.content or (';dr') in message.content:
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title ='**Game: Dice Roll**', color=0xe9b820, description=":game_die: You rolled the number... %s" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value=";coinflip | Coin Flip \n ;8ball | 8 Ball", inline=True)
        await client.send_message(message.channel, embed=em)
    # Coin Flip
    elif (';coinflip') in message.content or (';cf') in message.content:
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title ='**Game: Coin Flip**', color=0xe9b820, description=":moneybag: You flipped... %s" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value=";dicerole | Dice Roll \n ;8ball | 8 Ball", inline=True)
        await client.send_message(message.channel, embed=em)
    # 8 Ball
    elif (';8ball') in message.content or (';8b') in message.content:
        randomlist = ['It is certain.',
                      'It is decidedly so.',
                      'Without a doubt.',
                      'Yes - definitely.',
                      'You may rely on it.',
                      'As I see it, yes.',
                      'Most likely.',
                      'Outlook good.',
                      'Yes.',
                      'Signs point to yes.',
                      'Reply hazy, try again',
                      'Ask again later.',
                      'Better not tell you now.',
                      'Cannot predict now.',
                      'Concentrate and ask again.',
                      "Don't count on it.",
                      'My reply is no.',
                      'My sources say no.',
                      'Outlook not so good.',
                      'Very doubtful.',
                     ]
        em = discord.Embed(title ='**Game: 8 Ball**', color=0xe9b820, description=":8ball: *shake, shake* your answer is... %s" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value=";dicerole | Dice Roll \n ;coinflip | Coin Flip", inline=True)
        await client.send_message(message.channel, embed=em)
    # Russian Roulette
        # coming soon #
      
# Help
    if (';help') in message.content:
        em = discord.Embed(title="Discord Server", description="For any other help please join our Discord server...", url="https://discord.gg/eRHsyFg", color=0xe9b820)
        em.add_field(name="Prefix:", value="`;`", inline=True)
        em.add_field(name="Commands:", value="`;<command>`", inline =True)
        em.add_field(name="greet", value="Sends a greeting in the channel.", inline=False)
        em.add_field(name="invite", value="Sends the invite to add Sector Bot to your server.", inline=False)
        em.add_field(name="servercount", value="Shows how many servers this bot occupies.", inline=False)
        em.add_field(name="version", value="The current version of Sector Bot", inline=False)
        em.add_field(name="vote", value="Vote for this bot.", inline=False)
        em.add_field(name="meme", value="Sends a random meme from Sector Bot’s stash.", inline=False)
        em.add_field(name="say <text>", value="rewrites your text.", inline=False)
        em.add_field(name="purge <amount>", value="purges a specific amount of messages in a channel", inline=False)
        em.add_field(name="password", value="Generates a random password.", inline=False)
        em.add_field(name="diceroll / dr", value="Rolls a six sided die.", inline=False)
        em.add_field(name="coinflip / cf", value="Flips a coin, could be heads could be tails.", inline=False)
        em.add_field(name="8ball / 8b", value="Ask a question and shake the 8 Ball.", inline=False)
        await client.send_message(message.channel, embed=em)

#Bot Token
client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))
