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
client = commands.Bot(command_prefix = '?')
Clientdiscord = discord.Client()
servers = list(client.servers)

status = ['for: s/help | v0.2.2', 'for bot suggestions', 'for @Relyk-x#2896']
# WATCHING 'over ' + str(len(bot.servers)) + ' servers' ## v0.2.2,5##

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
    print("Connected on " + str(len(bot.servers)) + " servers:")
    for x in range(len(servers)):
     print(' ' + servers[x-1].name)
    await client.send_message(member, "Hey there I'm Sector Bot")
async def on_ready():
   print('Sector Bot is up and running with ' + str(len(client.servers)) + ' servers connected!')
    
# Purge
#@client.event
#async def on_purge(message):
#    if message.content.startswith('s/purge ') and not message.content[8:]=='':
#        message_amount = int(message.content[8:])
#        deleted = await bot.purge_from(message.channel, limit=message_amount, check=on_purge)
#       await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
# Say
#@client.event
#async def on_say(message):
#    if content.startswith('s/say '):
#        con = message.content
#        await client.send_message(message.channel, con[6:])

# Multiple Commands
@client.event
async def on_message(message):
    content = message.content
    
    # Purge
    if message.content.startswith('?purge ') and not message.content[7:]=='':
        message_amount = int(message.content[7:])
        deleted = await client.purge_from(message.channel, limit=message_amount, check=on_message)
        em = discord.Embed(description='Purged {} message(s) from this channel ⚠'.format(len(deleted)), color=0xb8ff00,)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        selfdel = await client.send_message(message.channel, embed=em)
        await asyncio.sleep(10)
        await client.delete_message(selfdel)
    # Say
    if content.startswith('?say '):
        await client.send_message(message.channel, content[5:])
        await client.delete_message(message)
    # Memes
    if ('?meme') in message.content:
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
        em = discord.Embed(title= 'Meme:', color=0xb8ff00,)
        em.set_image(url='%s' %(random.choice(randomlist),))
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
    # Emoji Lettering
    if message.content.startswith('?emojify '):
        result = ''
        for letter in message.content[9:]:
            if letter in 'aA':
                result = result + '🅰'
            if letter in 'bB':
                result = result + '🅱'
            if letter in 'cC':
                result = result + '🅲'
            if letter in 'dD':
                result = result + '🅳'
            if letter in 'eE':
                result = result + '🅴'
            if letter in 'fF':
                result = result + '🅵'
            if letter in 'gG':
                result = result + '🅶'
            if letter in 'hH':
                result = result + '🅷'
            if letter in 'iI':
                result = result + '🅸'
            if letter in 'jJ':
                result = result + '🅹'
            if letter in 'Kk':
                result = result + '🅺'
            if letter in 'lL':
                result = result + '🅻'
            if letter in 'mM':
                result = result + '🅼'
            if letter in 'nN':
                result = result + '🅽'
            if letter in 'oO':
                result = result + '🅾'
            if letter in 'pP':
                result = result + '🅿'
            if letter in 'qQ':
                result = result + '🆀'
            if letter in 'rR':
                result = result + '🆁'
            if letter in 'sS':
                result = result + '🆂'
            if letter in 'tT':
                result = result + '🆃'
            if letter in 'uU':
                result = result + '🆄'
            if letter in 'Vv':
                result = result + '🆅'
            if letter in 'wW':
                result = result + '🆆'
            if letter in 'xX':
                result = result + '🆇'
            if letter in 'Yy':
                result = result + '🆈'
            if letter in 'zZ':
                result = result + '🆉'
            if letter in '1':
                result = result + '1️⃣'
            if letter in '2':
                result = result + '2️⃣'
            if letter in '3':
                result = result + '3️⃣'
            if letter in '4':
                result = result + '4️⃣'
            if letter in '5':
                result = result + '5️⃣'
            if letter in '6':
                result = result + '6️⃣'
            if letter in '7':
                result = result + '7️⃣'
            if letter in '8':
                result = result + '8️⃣'
            if letter in '9':
                result = result + '9️⃣'
            if letter in '0':
                result = result + '0️⃣'
            if letter in ' ':
                result = result + ' '
            if letter in '@':
                result = result + '🕒'
            if letter in '!':
                result = result + '❗️'
            if letter in '.':
                result = result + '▫️'
            if letter in ',':
                result = result + '🔸'
            if letter in '#':
                result = result + '#️⃣'
            if letter in '$':
                result = result + '💲'
            if letter in '%':
                result = result + '💮'
            if letter in '^':
                result = result + '🔺'
            if letter in '&':
                result = result + '🌀'
            if letter in '?':
                result = result + '❔'
        await client.send_message(message.channel, result)
        await client.delete_message(message)
    # Tiny Letters
    if message.content.startswith('?compress '):
        result = ''
        for letter in message.content[10:]:
            if letter in 'aA':
                result = result + 'ᴀ'
            if letter in 'bB':
                result = result + 'ʙ'
            if letter in 'cC':
                result = result + 'ᴄ'
            if letter in 'dD':
                result = result + 'ᴅ'
            if letter in 'eE':
                result = result + 'ᴇ'
            if letter in 'fF':
                result = result + 'ғ'
            if letter in 'gG':
                result = result + 'ɢ'
            if letter in 'hH':
                result = result + 'ʜ'
            if letter in 'iI':
                result = result + 'ɪ'
            if letter in 'jJ':
                result = result + 'ᴊ'
            if letter in 'Kk':
                result = result + 'ᴋ'
            if letter in 'lL':
                result = result + 'ʟ'
            if letter in 'mM':
                result = result + 'ᴍ'
            if letter in 'nN':
                result = result + 'ɴ'
            if letter in 'oO':
                result = result + 'ᴏ'
            if letter in 'pP':
                result = result + 'ᴘ'
            if letter in 'qQ':
                result = result + 'ǫ'
            if letter in 'rR':
                result = result + 'ʀ'
            if letter in 'sS':
                result = result + 's'
            if letter in 'tT':
                result = result + 'ᴛ'
            if letter in 'uU':
                result = result + 'ᴜ'
            if letter in 'Vv':
                result = result + 'ᴠ'
            if letter in 'wW':
                result = result + 'ᴡ'
            if letter in 'xX':
                result = result + 'x'
            if letter in 'Yy':
                result = result + 'ʏ'
            if letter in 'zZ':
                result = result + 'ᴢ'
            if letter in '1':
                result = result + '➊'
            if letter in '2':
                result = result + '➋'
            if letter in '3':
                result = result + '➌'
            if letter in '4':
                result = result + '➍'
            if letter in '5':
                result = result + '➎'
            if letter in '6':
                result = result + '➏'
            if letter in '7':
                result = result + '➐'
            if letter in '8':
                result = result + '➑'
            if letter in '9':
                result = result + '➒'
            if letter in '0':
                result = result + '⓪'
            if letter in ' ':
                result = result + ' '
            if letter in '@':
                result = result + '@'
            if letter in '!':
                result = result + '!'
            if letter in '.':
                result = result + '.'
            if letter in ',':
                result = result + ','
            if letter in '#':
                result = result + '#'
            if letter in '$':
                result = result + '$'
            if letter in '%':
                result = result + '%'
            if letter in '^':
                result = result + '^'
            if letter in '&':
                result = result + '&'
            if letter in '?':
                result = result + '?'
        await client.send_message(message.channel, result)
        await client.delete_message(message)
    # Password Generator
    if ('?password') in message.content:
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
        em = discord.Embed(description='Here is your randomly generated password: ' + '`' + encryptedpass + '`', color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.author, embed=em)
        f = open('authpass.txt','a')
        f.write('\n' + 'Password: ' + encryptedpass + ' was generated by ' + str(message.author))
        f.close()
    # Invite
    if ('?invite') in message.content:
        em = discord.Embed(description="If you'd like to add Sector Bot to your server, Click here: https://goo.gl/2rp6n2", color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
    # Server Count
    if ('?servercount') in message.content:
        em = discord.Embed(description='Currently watching over ' + str(len(client.servers)) + ' servers', color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
    # Hello
    if ('?greet') in message.content:
        em = discord.Embed(description='Hey there buddy! :wave:', color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
    # Vote
    if ('?vote') in message.content:
        em = discord.Embed(description='You can vote here: https://discordbots.org/bot/496214977267630080/vote', color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
##### Version
    if ('?version') in message.content:
        em = discord.Embed(description='The current version of Sector Bot is: `v0.2.2`', color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        await client.send_message(message.channel, embed=em)
    # Dice Roll
    if ('?diceroll') in message.content or ('?dr') in message.content:
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title ='**Game: Dice Roll**', color=0xb8ff00, description="<:die:500434709835153408> You rolled the number... %s" %(random.choice(randomlist),))
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        em.add_field(name="Other Games:", value="s/coinflip | Coin Flip", inline=True)
        await client.send_message(message.channel, embed=em)
    # Coin Flip
    elif ('?coinflip') in message.content or ('?cf') in message.content:
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title ='**Game: Coin Flip**', color=0xb8ff00, description="<:token:500434456734203904> You flipped... %s" %(random.choice(randomlist),))
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        em.add_field(name="Other Games:", value="s/dicerole | Dice Roll", inline=True)
        await client.send_message(message.channel, embed=em)
    # Russian Roulette
        # coming soon #
# Helo
    if ('?help') in message.content:
        em = discord.Embed(title="Discord Server", description="For any other help please join our Discord server...", url="https://discord.gg/eRHsyFg", color=0xb8ff00)
        em.set_author(name="Sector Bot", icon_url="https://goo.gl/34WWBc")
        em.add_field(name="Prefix:", value="`?`", inline=True)
        em.add_field(name="Commands:", value="`?<command>`", inline =True)
        em.add_field(name="greet", value="Sends a greeting in the channel.", inline=False)
        em.add_field(name="invite", value="Sends the invite to add Sector Bot to your server.", inline=False)
        em.add_field(name="servercount", value="Shows how many servers this bot occupies.", inline=False)
        em.add_field(name="version", value="The current version of Sector Bot", inline=False)
        em.add_field(name="vote", value="Vote for this bot.", inline=False)
        em.add_field(name="meme", value="Sends a random meme from Sector Bot’s stash.", inline=False)
        em.add_field(name="emojify <text>", value="Emojifies your text.", inline=False)
        em.add_field(name="compress <text>", value="compresses your text to make it smaller.", inline=False)
        em.add_field(name="say <text>", value="rewrites your text.", inline=False)
        em.add_field(name="purge <amount>", value="purges a specific amount of messages in a channel", inline=False)
        em.add_field(name="password", value="Generates a random password.", inline=False)
        em.add_field(name="diceroll", value="Rolls a six sided die.", inline=False)
        em.add_field(name="coinflip", value="Flips a coin, could be heads could be tails.", inline=False)
        await client.send_message(message.channel, embed=em)

#Bot Token
client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))
