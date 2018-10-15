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

status = ['for: s/help | v0.1.7', 'for bot suggestions',]
# WATCHING 'over ' + str(len(client.servers)) + ' servers' ## v0.1.7,6 ##

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
    print("Connected on " + str(len(client.servers)) + " servers:")
    for x in range(len(servers)):
     print(' ' + servers[x-1].name)
    await client.send_message(member, "Hey there I'm Sector Bot")
async def on_ready():
   print('Sector Bot is up and running with ' + str(len(client.servers)) + ' servers connected!')

em = discord.Embed

# Multiple Commands
@client.event
async def on_message(message):
    # Memes
    if ('s/meme') in message.content:
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
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.channel, embed=em)
    # Re Write
    if message.content.startswith('s/rewrite '):
        result = ''
        for letter in message.content[10:]:
            if letter in 'A':
                result = result + 'A'
            if letter in 'a':
                result = result + 'a'
            if letter in 'B':
                result = result + 'B'
            if letter in 'b':
                result = result + 'b'
            if letter in 'C':
                result = result + 'C'
            if letter in 'c':
                result = result + 'c'
            if letter in 'D':
                result = result + 'D'
            if letter in 'd':
                result = result + 'd'
            if letter in 'E':
                result = result + 'E'
            if letter in 'e':
                result = result + 'e'
            if letter in 'F':
                result = result + 'F'
            if letter in 'f':
                result = result + 'f'
            if letter in 'G':
                result = result + 'G'
            if letter in 'g':
                result = result + 'g'
            if letter in 'H':
                result = result + 'H'
            if letter in 'h':
                result = result + 'h'
            if letter in 'I':
                result = result + 'I'
            if letter in 'i':
                result = result + 'i'
            if letter in 'J':
                result = result + 'J'
            if letter in 'j':
                result = result + 'j'
            if letter in 'K':
                result = result + 'K'
            if letter in 'k':
                result = result + 'k'
            if letter in 'L':
                result = result + 'L'
            if letter in 'l':
                result = result + 'l'
            if letter in 'M':
                result = result + 'M'
            if letter in 'm':
                result = result + 'm'
            if letter in 'N':
                result = result + 'N'
            if letter in 'n':
                result = result + 'n'
            if letter in 'O':
                result = result + 'O'
            if letter in 'o':
                result = result + 'o'
            if letter in 'P':
                result = result + 'P'
            if letter in 'p':
                result = result + 'p'
            if letter in 'Q':
                result = result + 'Q'
            if letter in 'q':
                result = result + 'q'
            if letter in 'R':
                result = result + 'R'
            if letter in 'r':
                result = result + 'r'
            if letter in 'S':
                result = result + 'S'
            if letter in 's':
                result = result + 's'
            if letter in 'T':
                result = result + 'T'
            if letter in 't':
                result = result + 't'
            if letter in 'U':
                result = result + 'U'
            if letter in 'u':
                result = result + 'u'
            if letter in 'V':
                result = result + 'V'
            if letter in 'v':
                result = result + 'v'
            if letter in 'W':
                result = result + 'W'
            if letter in 'w':
                result = result + 'w'
            if letter in 'X':
                result = result + 'X'
            if letter in 'x':
                result = result + 'x'
            if letter in 'Y':
                result = result + 'Y'
            if letter in 'y':
                result = result + 'y'
            if letter in 'Z':
                result = result + 'Z'
            if letter in 'z':
                result = result + 'z'
            if letter in '1':
                result = result + '1'
            if letter in '2':
                result = result + '2'
            if letter in '3':
                result = result + '3'
            if letter in '4':
                result = result + '4'
            if letter in '5':
                result = result + '5'
            if letter in '6':
                result = result + '6'
            if letter in '7':
                result = result + '7'
            if letter in '8':
                result = result + '8'
            if letter in '9':
                result = result + '9'
            if letter in '0':
                result = result + '0'
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
            if letter in '*':
                result = result + '*'
            if letter in '(':
                result = result + '('
            if letter in ')':
                result = result + ')'
            if letter in '-':
                result = result + '-'
            if letter in '+':
                result = result + '+'
            if letter in '_':
                result = result + '_'
            if letter in '=':
                result = result + '='
            if letter in '[':
                result = result + '['
            if letter in ']':
                result = result + ']'
            if letter in '{':
                result = result + '{'
            if letter in '}':
                result = result + '}'
            if letter in ';':
                result = result + ';'
            if letter in ':':
                result = result + ':'
            if letter in '|':
                result = result + '|'
            if letter in '<':
                result = result + '<'
            if letter in '>':
                result = result + '>'
            if letter in '`':
                result = result + '`'
            if letter in '~':
                result = result + '~'
            if letter in '?':
                result = result + '?'
        await client.send_message(message.channel, result)
        await client.delete_message(message)
    # Emoji Lettering
    if message.content.startswith('s/emojify '):
        result = ''
        for letter in message.content[10:]:
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
    if message.content.startswith('s/compress '):
        result = ''
        for letter in message.content[11:]:
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
    if ('s/password') in message.content:
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
        em = discord.Embed(description='Here is your randomly generated password: ' + '`' + encryptedpass + '`', color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.author, embed=em)
        f = open('authpass.txt','a')
        f.write('\n' + 'Password: ' + encryptedpass + ' was generated by ' + str(message.author))
        f.close()
    # Invite
    if ('s/invite') in message.content:
        em = discord.Embed(description="If you'd like to add Sector Bot to your server, Click here: https://goo.gl/2rp6n2", color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.channel, embed=em)
    # Server Count
    if ('s/servercount') in message.content:
        em = discord.Embed(description='Currently watching over ' + str(len(client.servers)) + ' servers', color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.channel, embed=em)
    # Hello
    if ('s/greet') in message.content:
        em = discord.Embed(description='Hey there buddy! :wave:', color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.channel, embed=em)
    # Purge
    if message.content == 's/purge':
        deleted = await client.purge_from(message.channel, limit=100, check=on_message)
        await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
    # Vote
    if ('s/vote') in message.content:
        em = discord.Embed(description='You can vote here: https://discordbots.org/bot/496214977267630080/vote', color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.channel, embed=em)
##### Version
    if ('s/version') in message.content:
        em = discord.Embed(description='The current version of Sector Bot is: `v0.1.7`', color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        await client.send_message(message.channel, embed=em)
    # Dice Roll
    if ('s/diceroll') in message.content or ('s/dr') in message.content:
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title ='**Game: Dice Roll**', color=0xffffff, description="<:die:500434709835153408> You rolled the number... %s" %(random.choice(randomlist),))
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        em.add_field(name="Other Games:", value="s/coinflip | Coin Flip", inline=True)
        await client.send_message(message.channel, embed=em)
    # Coin Flip
    elif ('s/coinflip') in message.content or ('s/cf') in message.content:
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title ='**Game: Coin Flip**', color=0xffffff, description="<:token:500434456734203904> You flipped... %s" %(random.choice(randomlist),))
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        em.add_field(name="Other Games:", value="s/dicerole | Dice Roll", inline=True)
        await client.send_message(message.channel, embed=em)
    # Russian Roulette
        # coming soon #
# Helo
    if ('s/help') in message.content:
        em = discord.Embed(title="Discord Server", description="For any other help please join our Discord server...", url="https://discord.gg/eRHsyFg", color=0xffffff)
        em.set_author(name="Sector Bot", icon_url="https://cdn.discordapp.com/attachments/499771629396688909/500484058367655945/arrow.png")
        em.add_field(name="Prefix:", value="`s/`", inline=True)
        em.add_field(name="Commands:", value="`s/<command>`", inline =True)
        em.add_field(name="s/greet", value="Sends a greeting in the channel.", inline=False)
        em.add_field(name="s/invite", value="Sends the invite to add Sector Bot to your server.", inline=False)
        em.add_field(name="s/servercount", value="Shows how many servers this bot occupies.", inline=False)
        em.add_field(name="s/version", value="The current version of Sector Bot", inline=False)
        em.add_field(name="s/vote", value="Vote for this bot.", inline=False)
        em.add_field(name="s/meme", value="Sends a random meme from Sector Bot’s stash.", inline=False)
        em.add_field(name="s/emojify <text>", value="Emojifies your text.", inline=False)
        em.add_field(name="s/compress <text>", value="compresses your text to make it smaller.", inline=False)
        em.add_field(name="s/rewrite <text>", value="rewrites your text.", inline=False)
        em.add_field(name="s/password", value="Generates a random password.", inline=False)
        em.add_field(name="s/diceroll", value="Rolls a six sided die.", inline=False)
        em.add_field(name="s/coinflip", value="Flips a coin, could be heads could be tails.", inline=False)
        await client.send_message(message.channel, embed=em)

#Bot Token
client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))
