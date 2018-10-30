# Initialise
import discord
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
from itertools import cycle
import json
import os
import urllib3

http = urllib3.PoolManager()

url = "https://api.thecatapi.com/v1/images/search"

querystring = {"format":"json"}

headers = {
    'Content-Type': "application/json",
    'x-api-key': "bc77e012-c69d-4dc9-ba73-42e710028838"
    }


Client = discord.client
client = commands.Bot(command_prefix = ';')
Clientdiscord = discord.Client()

# Setting Bot status 'Watching'
async def change_status():
  await client.wait_until_ready()
  status = ['for: ;help | v0.2.5', 'for: bot suggestions', 'for: @Relyk-x#2896']
# WATCHING 'over ' + str(len(bot.servers)) + ' servers' ## v0.2.5,8##
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
#    if message.content.startswith(';purge ') and not message.content[7:]=='':
#        message_amount = int(message.content[7:])
#        deleted = await client.purge_from(message.channel, limit=message_amount, check=on_message)
#        em = discord.Embed(description='Purged {} message(s) from this channel ⚠'.format(len(deleted)), color=0xffafc9,)
#        selfdel = await client.send_message(message.channel, embed=em)
#        await asyncio.sleep(10)
#        await client.delete_message(selfdel)
        
    # Say
    content = message.content
    if content.startswith(';say '):
        await client.send_message(message.channel, content[5:])
        await client.delete_message(message)
    
    # Oofify
    if message.content.startswith(';oofify '):
        result = ''
        for letter in message.content[8:]:
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
        asyncio.sleep(2)
        oofmsg = await client.send_message(message.channel,'Processing > ☑️')
        asyncio.sleep(5)
        await client.edit_message(oofmsg,"Error > ❌ > [Invalid Characters detected]")
        asyncio.sleep(1)
        await client.edit_message(oofmsg, result)
        await client.delete_message(message)
    
    # Tiny Caps
    if message.content.startswith(';tiny '):
        result = ''
        for letter in message.content[6:]:
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
    
    # Memes
    if (';meme') in message.content:
        randomlist = ['https://goo.gl/1wezZw',  #Dr. Phill
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
        em = discord.Embed(title= 'Meme:', color=0xffafc9,)
        em.set_image(url='%s' %(random.choice(randomlist),))
        await client.send_message(message.channel, embed=em)
    
    # Greyscale Wallpaper
    if message.content == ';gswallpaper':
        em = discord.Embed(description='Right click and then click open link in order to get redirected to the page and download it :yum: ')
        em.set_image(url='https://picsum.photos/g/1280/720/?image=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)
        
    # Greyscale Image
    if message.content == ';gsimg':
        em = discord.Embed(description='Fresh Grayscale image to fit your photo frame! ')
        em.set_image(url='https://picsum.photos/g/200/300/?image=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)
        
    # Random Wallpaper
    if message.content == ';randwallpaper':
        em = discord.Embed(description='Right click and then click open link in order to get redirected to the page and download it :yum: ')
        em.set_image(url='https://picsum.photos/1280/720/?image=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)

    # Random Image
    if message.content == ';randimg':
        em = discord.Embed(description='Fresh image to fit your photo frame! ')
        em.set_image(url='https://picsum.photos/200/300/?image=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)
    
    # Blur Wallpaper
    if message.content == ';blurwallpaper':
        em = discord.Embed(description='Right click and then click open link in order to get redirected to the page and download it :yum: ')
        em.set_image(url='https://picsum.photos/1280/720/?blur=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)
    
    # Blur Image
    if message.content == ';blurimg':
        em = discord.Embed(description='Fresh Blurry image to fit your photo frame! ')
        em.set_image(url='https://picsum.photos/200/300/?blur=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)
    
    # Random Gif
    if message.content == ';randgif':
        em = discord.Embed(description='Here is a fun gif i just randomly generated for you :)')
        em.set_image(url='http://replygif.net/i/' + str(random.randint(90, 1100)) + '.gif')
        await client.send_message(message.channel, embed=em)
    
    
    # Random Kitten - http://www.randomkittengenerator.com/cats/rotator.php
    if message.content == ';kitten':
        r = http.request('GET', 'https://api.thecatapi.com/v1/images/search')
        await client.send_message(message.channel,r.data)
    
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
        em = discord.Embed(description='Here is your randomly generated password: ' + '`' + encryptedpass + '`', color=0xffafc9)
        await client.send_message(message.author, embed=em)
        f = open('authpass.txt','a')
        f.write('\n' + 'Password: ' + encryptedpass + ' was generated by ' + str(message.author))
        f.close()
        
    # Invite
    if (';invite') in message.content:
        em = discord.Embed(description="If you'd like to add Sector Bot to your server, Click here: https://goo.gl/2rp6n2", color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
    # Server Count
    if (';servercount') in message.content:
        em = discord.Embed(description='Currently watching over ' + str(len(client.servers)) + ' Discord servers <:discord:501956002158215198>', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
    # Greet
    if (';greet') in message.content:
        em = discord.Embed(description='Hey there buddy! :wave:', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
    # Vote
    if (';vote') in message.content:
        em = discord.Embed(description='You can vote here: https://discordbots.org/bot/496214977267630080/vote', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
##### Version
    if (';version') in message.content:
        em = discord.Embed(description='The current version of Sector Bot is: `v0.2.5`', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
    
    # Dice Roll
    if (';diceroll') in message.content or (';dr') in message.content:
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title ='**Game: Dice Roll**', color=0xffafc9, description=":game_die: You rolled the number... %s" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value=";coinflip | Coin Flip \n ;8ball | 8 Ball", inline=True)
        await client.send_message(message.channel, embed=em)
    
    # Coin Flip
    elif (';coinflip') in message.content or (';cf') in message.content:
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title ='**Game: Coin Flip**', color=0xffafc9, description=":moneybag: You flipped... %s" %(random.choice(randomlist),))
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
        em = discord.Embed(title ='**Game: 8 Ball**', color=0xffafc9, description=":8ball: *shake, shake* your answer is... %s" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value=";dicerole | Dice Roll \n ;coinflip | Coin Flip", inline=True)
        await client.send_message(message.channel, embed=em)
    # Russian Roulette
        # coming soon #
      
# Help
    if (';help') in message.content:
        em = discord.Embed(title="- click here for help -", description="For any other help please join our Discord server...", url="https://discord.gg/eRHsyFg", color=0xffafc9)
        em.set_author(name="MikiBot", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
        em.add_field(name="Prefix:", value="`;`", inline=True)
        em.add_field(name="Commands:", value="`;<command>`", inline =True)
        em.add_field(name="greet", value="Sends a greeting in the channel.", inline=False)
        em.add_field(name="invite", value="Sends the invite to add Sector Bot to your server.", inline=False)
        em.add_field(name="servercount", value="Shows how many servers this bot occupies.", inline=False)
        em.add_field(name="version", value="The current version of Sector Bot", inline=False)
        em.add_field(name="vote", value="Vote for this bot.", inline=False)
        em.add_field(name="meme", value="Sends a random meme from Sector Bot’s stash.", inline=False)
        em.add.field(name="kitten", value="Sends a random pic of a kitten.", inline=False)
        em.add_field(name="randimg", value="Generates a random image.", inline=False)
        em.add_field(name="randwallpaper", value="Generate a random wallpaper.", inline=False)
        em.add_field(name="blurwallpaper", value="Generate a random wallpaper.", inline=False)
        em.add_field(name="gswallpaper", value="Generate a random wallpaper.", inline=False)
        em.add_field(name="gsimg", value="Generate a random image.", inline=False)
        em.add_field(name="blurimg", value="Generate a random image.", inline=False)
        em.add_field(name="randgif", value="Generate a random image.", inline=False)
        em.add_field(name="oofify", value="Emojifies your text.", inline=False)
        em.add_field(name="tiny", value="Decorates your text.", inline=False)
        em.add_field(name="say <text>", value="rewrites your text.", inline=False)
        em.add_field(name="purge <amount>", value="`DISABLED`", inline=False) #purges a specific amount of messages in a channel
        em.add_field(name="password", value="Generates a random password.", inline=False)
        em.add_field(name="diceroll / dr", value="Rolls a six sided die.", inline=False)
        em.add_field(name="coinflip / cf", value="Flips a coin, could be heads could be tails.", inline=False)
        em.add_field(name="8ball / 8b", value="Ask a question and shake the 8 Ball.", inline=False)
        await client.send_message(message.channel, embed=em)
    #if ('!help') in message.content:
        #em = discord.Embed(title="https://rythmbot.co/", description="Commands for Rythm bot...", url="https://rythmbot.co/", colour=0xff0000)
        #em.set_author(name="Rythm Bot", url="https://rythmbot.co/", icon_url="https://rythmbot.co/assets/img/rythm-header.png")
        #em.add_field(name="Prefix:", value="`!`", inline=True)
        #em.add_field(name="Commands:", value="`!<command>`", inline =True)
        #em.add_field(name="play", value="Plays a song with the given name or url.", inline=False)
        #em.add_field(name="disconnect",	value="Disconnect the bot from the voice channel it is in.", inline=False)
        #em.add_field(name="np", value="Shows what song the bot is currently playing.", inline=False)
        #em.add_field(name="aliases", value="List command aliases.", inline=False)
        #em.add_field(name="ping", value="Checks the bot's response time to Discord.", inline=False)
        #em.add_field(name="skip", value="Skips the currently playing song.", inline=False)
        #em.add_field(name="seek", value="Seeks to a certain point in the current track.", inline=False)
        #em.add_field(name="soundcloud", value="Searches soundcloud for a song.", inline=False)
        #em.add_field(name="remove", value="Removes a certain entry from the queue.", inline=False)
        #em.add_field(name="loopqueue", value="Loops the whole queue.", inline=False)
        #em.add_field(name="search", value="Searches YouTube for results of a URL.", inline=False)
        #em.add_field(name="stats", value="Shows the stats of the bot.", inline=False)
        #em.add_field(name="loop", value="Loop the currently playing song.", inline=False)
        #em.add_field(name="donate", value="Info about donating to support Rythm!", inline=False)
        #em.add_field(name="shard", value="Checks the shard you are on.", inline=False)
        #em.add_field(name="join", value="Summons the bot to your voice channel.", inline=False)
        #em.add_field(name="lyrics", value="Gets the lyrics of the current playing song.", inline=False)
        #em.add_field(name="info", value="Info about Rythm!", inline=False)
        #em.add_field(name="resume", value="Resume paused music.", inline=False)
        #em.add_field(name="settings", value="Change Rythm's settings.", inline=False)
        #em.add_field(name="move", value="Moves a certain song to the first position in the queue or to a chosen position.", inline=False)
        #em.add_field(name="forward", value="Forwards by a certain amount in the current track.", inline=False)
        #em.add_field(name="skipto",	value="Skips to a certain position in the queue.", inline=False)
        #em.add_field(name="clear", value="Clears the queue.", inline=False)
        #em.add_field(name="replay", value="Reset the progress of the current song", inline=False)
        #em.add_field(name="clean", value="Deletes the bot's messages and commands.", inline=False)
        #em.add_field(name="pause", value="Pauses the currently playing track.", inline=False)
        #em.add_field(name="removedupes", value="Removes duplicate songs from the queue.", inline=False)
        #em.add_field(name="volume", value="Check or change the current volume.", inline=False)
        #em.add_field(name="rewind", value="Rewinds by a certain amount in the current track.", inline=False)
        #em.add_field(name="playtop", value="Like the play command, but queues from the top.", inline=False)
        #em.add_field(name="playskip", value="Adds a song to the top of the queue then skips to it.", inline=False)
        #em.add_field(name="invite", value="Links!", inline=False)
        #em.add_field(name="shuffle", value="Shuffles the queue.", inline=False)
        #em.add_field(name="queue", value="View the queue. To view different pages, type the command with the specified page number after it (queue 2).", inline=False)
        #em.add_field(name="leavecleanup", value="Removes absent user's songs from the Queue.", inline=False)
        #await client.send_message(message.channel, embed=em)
#Bot Token
client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))
