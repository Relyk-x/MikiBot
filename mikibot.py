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
import bs4, requests
from time import gmtime, strftime

FORTNITE_API_TOKEN = os.getenv('FORTNITETOKEN')
COMMAND_PREFIX = ';'
VERSION = 'v0.4.1' #v0.4.1,8

querystring = {"format":"json"}

headers = {
    'Content-Type': "application/json",
    'x-api-key': "bc77e012-c69d-4dc9-ba73-42e710028838"
    }
def fortnite_tracker_api(platform, nickname):
  URL = 'https://api.fortnitetracker.com/v1/profile/' + platform + '/' + nickname
  req = requests.get(URL, headers={"TRN-Api-Key": FORTNITE_API_TOKEN})

  if req.status_code == 200:
    try:
      print(req.json())
      lifetime_stats = req.json()['lifeTimeStats']
      return lifetime_stats[7:]
    except KeyError:
      return False
  else:
    return False

Client = discord.client
client = commands.Bot(command_prefix = ';')
Clientdiscord = discord.Client()

# Setting Bot status 'Watching'
async def change_status():
  await client.wait_until_ready()
  servers = list(client.servers)
  status = ['for ;help | ' + VERSION, 'for bot suggestions', 'for @Relyk-x#2896']
# WATCHING 'over ' + str(len(bot.servers)) + ' servers'
# WATCHING 'for: ;help | ' + VERSION, 'for: bot suggestions', 'for: @Relyk-x#2896'
  msgs = cycle(status)

  while not client.is_closed:
     current_status = next(msgs)
     await client.change_presence(game=discord.Game(name=current_status, url="https://www.twitch.tv/streamer",type=3))
     await asyncio.sleep(10)
      
# Start Up
@client.event
async def on_member_join(member):
    servers = list(client.servers)
    print("Connected on " + str(len(client.servers)) + " servers:")
    for x in range(len(servers)):
     print(' ' + servers[x-1].name)
    await client.send_message(member, "Hey there I'm MikiBot")
    
# Checking if bot is online    
async def on_ready():
   print('MikiBot is up and running with ' + str(len(client.servers)) + ' servers connected!')

# Multiple Commands
@client.event
async def on_message(message):
    
    # Purge
    if message.content.startswith(';purge ') or message.content.startswith(';purge'):
         await client.send_message(message.channel, '`PURGE: DISABLED`')
    
    # Say
    content = message.content
    if content.startswith(';say '):
        await client.send_message(message.channel, content[5:])
        await client.delete_message(message)
        
    # About
    if message.content == ';about':
        em = discord.Embed(title="https://discord.gg/UjuGRB9", description="For any other help please join our Discord server...", url="https://discord.gg/UjuGRB9", color=0xffafc9)
        em.set_author(name="MikiBot", url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
        em.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use ;help to see what else I can do for you~ \n\n<:curiouscat:508516637700259850> Curious Cat: https://curiouscat.me/MikiDiscord \n - If you have any questions please ask here. \n\n<:twitter:508515087330312193> Twitter: https://twitter.com/MikiDiscord \n - You can follow me on twitter here.", inline=False)
        em.set_footer(text="version: " + VERSION)
        await client.send_message(message.channel, embed=em)
    
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
    if message.content == ';meme':
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
        em = discord.Embed(title='Meme:', color=0xffafc9,)
        em.set_image(url='%s' %(random.choice(randomlist),))
        await client.send_message(message.channel, embed=em)
        
    # Random Wallpaper
    if message.content == ';wallpaper':
        em = discord.Embed(title='Wallpaper:', color=0xffafc9,)
        em.set_image(url='https://picsum.photos/1280/720/?image=' + str(random.randint(1, 999)))
        await client.send_message(message.channel, embed=em)
        
    # Random Gif
    if message.content == ';gif':
        em = discord.Embed(title='Gif:', color=0xffafc9,)
        em.set_image(url='http://replygif.net/i/' + str(random.randint(90, 1100)) + '.gif')
        await client.send_message(message.channel, embed=em)
    
    # Password Generator
    if message.content == ';password':
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
    if message.content == ';invite':
        em = discord.Embed(description="If you'd like to add Sector Bot to your server, Click here: https://goo.gl/2rp6n2", color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
    # Server Count
    if message.content == ';servercount':
        em = discord.Embed(description='Currently watching over ' + str(len(client.servers)) + ' Discord servers <:discord:501956002158215198>', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
    # Server List
    if message.content.startswith(';serverlist'):
        servers = list(client.servers)
        em = discord.Embed(description='Currently watching over ' + str(len(client.servers)) + ' Discord servers <:discord:501956002158215198>', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        for x in range(len(servers)):
         await client.send_message(message.channel,('```md\n# ' + servers[x-1].name) + '\n ● ServerID: ' + servers[x-1].id + '```')
    
    # Greet
    if message.content == ';greet':
        await client.send_message(message.channel, 'H-hello >//<')
        
    # Vote
    if message.content == ';vote':
        em = discord.Embed(description='You can vote here: \n\n:point_right: https://discordbots.org/bot/496214977267630080/vote :point_left:', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
    
    # Donate
    if message.content == ';donate':
        em = discord.Embed(description='You can donate by purchasing roles from the MikiBot Help server here: \n\n:point_right: https://goo.gl/wGG82o :point_left:', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
        
##### Version
    if message.content == ';version':
        em = discord.Embed(description='The current version of Sector Bot is: `' + VERSION + '`', color=0xffafc9)
        await client.send_message(message.channel, embed=em)
    
    # Time
    if message.content == ';time':
        dash = strftime("%H:%M", gmtime())
        wholetime = dash[0] + dash[1]
        resttime = dash[2:]
        if int(wholetime) < 12:
            await client.send_message(message.channel, 'The server time now is: **' + wholetime + resttime + 'AM. GMTIME(0:00)**')
        else:
            await client.send_message(message.channel, 'The server time now is: **' + int(wholetime-12) + resttime + 'PM. GMTTIME(0:00)**')

    # YouTube
    if message.content.startswith(';youtube '):
        name = message.content[9:]
        fullcontent = ('http://www.youtube.com/results?search_query=' + name)
        text = requests.get(fullcontent).text
        soup = bs4.BeautifulSoup(text, 'html.parser')
        img = soup.find_all('img')
        div = [ d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
        img0 = div[0].find_all('img')[0]
        imgurl = (img0['src'])
        a = [ x for x in div[0].find_all('a') if x.has_attr('title') ]
        title = (a[0]['title'])
        a0 = [ x for x in div[0].find_all('a') if x.has_attr('title') ][0]
        url= ('http://www.youtube.com'+a0['href'])
        em = discord.Embed(title=title, url=url, color=0xffafc9)
        em.set_author(name='📺   YouTube Search')
        em.set_thumbnail(url=imgurl)
        em.add_field(name='Channel', value='<channel name>', inline=True)
        em.add_field(name='Duration', value='<duration of video>', inline=True)
        em.set_footer(text="not yet opperational...")
        await client.send_message(message.channel, embed=em)
    
    # Dice Roll
    if message.content == ';diceroll' or message.content == ';dr':
        randomlist = ['1','2','3','4','5','6',]
        em = discord.Embed(title ='**Game: Dice Roll**', color=0xffafc9, description="🎲 *rolls a dice* \n\nYou rolled a dice and it landed on a \n Side: **%s** \n ________________________________________" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value="Coin Flip | ;coinflip \n 8 Ball | ;8ball", inline=True)
        await client.send_message(message.channel, embed=em)
    
    # Coin Flip
    elif message.content == ';coinflip' or message.content == ';cf':
        randomlist = ['Heads','Tails',]
        em = discord.Embed(title ='**Game: Coin Flip**', color=0xffafc9, description="💰 *flips a coin* \n\nYou flipped a coin and it landed on \n Face: **%s** \n ________________________________________" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value="Dice Roll | ;dicerole \n 8 Ball | ;8ball", inline=True)
        await client.send_message(message.channel, embed=em)
    
    # 8 Ball
    elif message.content == ';8ball' or message.content == ';8b':
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
        em = discord.Embed(title ='**Game: 8 Ball**', color=0xffafc9, description="🎱 *shakes the 8 Ball up...*` \n\nYou shook the 8 ball and it shows you... \n Answer: **%s** \n ________________________________________" %(random.choice(randomlist),))
        em.add_field(name="Other Games:", value="Dice Roll | ;dicerole \n Coin Flip | ;coinflip", inline=True)
        await client.send_message(message.channel, embed=em)
      
    # Fortnite
    if message.content.startswith(COMMAND_PREFIX + 'fortnite'):
      words = message.content.split(' ', 2)

      if len(words) < 3:
        await client.send_message(message.channel, 'Usage: ' + COMMAND_PREFIX + 'fortnite `<pc | xbl | psn>` `<nickname>`')
        return

      platform = words[1].lower()

      # more acceptable platform names
      if platform == 'xbox':
        platform = 'xbl'
      elif platform == 'ps4':
        platform = 'psn'

      if platform not in ('pc','xbl','psn'):
        await client.send_message(message.channel, 'Usage: ' + COMMAND_PREFIX + 'fortnite `<pc | xbl | psn>` `<nickname>`')
        return
      else:
        res = fortnite_tracker_api(platform,words[2])

        if res:
          matches_played = res[0]['value']
          wins = res[1]['value']
          win_percent = res[2]['value']
          kills = res[3]['value']
          kd = res[4]['value']

          embed = discord.Embed(title="Lifetime Stats for " + words[2], color=0xffafc9)
            
          embed.add_field(name="Matches Played", value=matches_played + '\n', inline=False)
          embed.add_field(name="Wins", value=wins + '\n', inline=False)
          embed.add_field(name="Win percent", value=win_percent + '\n', inline=False)
          embed.add_field(name="Kills", value=kills + '\n', inline=False)
          embed.add_field(name="K/D", value=kd + '\n', inline=False)
          await client.send_message(message.channel, embed=embed)
        else:
          await client.send_message(message.channel, 'Failed to get data. Double check spelling of your nickname.')

########## COMMING SOON ##########

    # Games
        # Tic Tac Toe
        # Connect Four
        # Hang Man
        # Roulette
        # Russian Roulette
        # Blackjack
        # Paper Scissors Rock
        # Akinator
        # Cock Fight
        # Truth or Dare
        # Never Have I Ever
        # Slots
        # Dungeons and Dragons
        # Jokes
        
########## CUT OUT CONTENT NEEDS REVIEW #########

    # Purge
#   if message.content.startswith(';purge ') and not message.content[7:]=='':
#        message_amount = int(message.content[7:])
#        deleted = await client.purge_from(message.channel, limit=message_amount, check=on_message)
#        em = discord.Embed(description='Purged {} message(s) from this channel ⚠'.format(len(deleted)), color=0xffafc9,)
#        selfdel = await client.send_message(message.channel, embed=em)
#        await asyncio.sleep(10)
#        await client.delete_message(selfdel)

    # Greyscale Wallpaper
#    if message.content == ';gswallpaper':
#        em = discord.Embed(description='Right click and then click open link in order to get redirected to the page and download it :yum: ')
#        em.set_image(url='https://picsum.photos/g/1280/720/?image=' + str(random.randint(1, 999)))
#        await client.send_message(message.channel, embed=em)
        
    # Greyscale Image
#    if message.content == ';gsimg':
#        em = discord.Embed(description='Fresh Grayscale image to fit your photo frame! ')
#        em.set_image(url='https://picsum.photos/g/200/300/?image=' + str(random.randint(1, 999)))
#        await client.send_message(message.channel, embed=em)

    # Random Image
#    if message.content == ';randimg':
#        em = discord.Embed(description='Fresh image to fit your photo frame! ')
#        em.set_image(url='https://picsum.photos/200/300/?image=' + str(random.randint(1, 999)))
#        await client.send_message(message.channel, embed=em)
    
    # Blur Wallpaper
#    if message.content == ';blurwallpaper':
#        em = discord.Embed(description='Right click and then click open link in order to get redirected to the page and download it :yum: ')
#        em.set_image(url='https://picsum.photos/1280/720/?blur=' + str(random.randint(1, 999)))
#        await client.send_message(message.channel, embed=em)
    
    # Blur Image
#    if message.content == ';blurimg':
#        em = discord.Embed(description='Fresh Blurry image to fit your photo frame! ')
#        em.set_image(url='https://picsum.photos/200/300/?blur=' + str(random.randint(1, 999)))
#        await client.send_message(message.channel, embed=em)

      
# Help
    if message.content == ';help':
        em = discord.Embed(title="https://discord.gg/UjuGRB9", description="For any other help please join our Discord server...", url="https://discord.gg/UjuGRB9", color=0xffafc9)
        em.set_author(name="MikiBot", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
        # Bot
        em.add_field(name="Bot", value=" Prefix: `;` \n Commands: `;<command>` \n ________________________________________", inline=True)
        
        # Social
        em.add_field(name="💬 Social", value=" greet – Sends a greeting in the channel. \n oofify <text> – Emojifies your text. \n tiny <text> – Decorates your text. \n say <text> – rewrites your text. \n ________________________________________", inline=False)
        
        # Server
        em.add_field(name="📂 Server", value=" about – Shows the About description of MikiBot. \n invite – Sends the invite to add MikiBot to your server. \n servercount – Shows how many servers this bot occupies. \n version – The current version of MikiBot. \n vote – Vote for MikiBot. \n donate – Donate to MikiBot. \n purge <amount> – `DISABLED` \n ________________________________________", inline=False)
        #purges a specific amount of messages in a channel
        
        #Fun
        em.add_field(name="🎉 Fun", value=" meme – Sends a random meme from Sector Bot’s stash. \n password – Generates a random password. \n wallpaper – Generate a random wallpaper. \n gif – Generate a random gif. \n ________________________________________", inline=False)
        
        #Games
        em.add_field(name="🎭 Games", value=" diceroll – Rolls a six sided die. \n coinflip – Flips a coin, could be heads could be tails. \n 8ball – Ask a question and shake the 8 Ball. \n ________________________________________ \n\n<:curiouscat:508516637700259850> Curious Cat: https://curiouscat.me/MikiDiscord \n - If you have any questions please ask here. \n\n<:twitter:508515087330312193> Twitter: https://twitter.com/MikiDiscord \n - You can follow me on twitter here.", inline=False)
        
        em.set_footer(text="version: " + VERSION)
        await client.send_message(message.channel, embed=em)
    
#Bot Token
client.loop.create_task(change_status())
client.run(os.getenv('BOT_TOKEN'))
