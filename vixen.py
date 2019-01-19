##############################################################################################################################
# 🤖 | B O T - S T A R T U P
##############################################################################################################################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import datetime
from datetime import datetime
import time
import bs4, requests

import os

bot = commands.Bot(command_prefix=';')
msglimit = 100
now = datetime.now()
ver = "0.6.1"#1
botname = "Vixen"
pref = ";"
owner_id = "257784039795064833"

#Emoji
vixen = "https://cdn.discordapp.com/attachments/406045563814019093/406071077249482753/kami___render__185_by_starryskytrench-dbhote5.png"
warning = "https://cdn.discordapp.com/attachments/499771950764261396/515272525626867722/warning.png"
dis_cord = "https://cdn.discordapp.com/attachments/499771950764261396/500485578794729482/discord_logo1600.png"
clock = "https://cdn.discordapp.com/attachments/499771950764261396/515269664507691008/clock.png"
curiouscat = "https://cdn.discordapp.com/attachments/499771950764261396/514996231647395841/curiouscat.png"
twitter = "https://cdn.discordapp.com/attachments/499771950764261396/514996202719150088/twitter.png"
patreon = "https://cdn.discordapp.com/attachments/499771950764261396/513936104357888000/icon_color_variations.jpg"
general = "https://cdn.discordapp.com/attachments/499771950764261396/500485578794729482/discord_logo1600.png"
fun = "https://cdn.discordapp.com/attachments/499771950764261396/500485578794729482/discord_logo1600.png"
you_be = "https://cdn.discordapp.com/attachments/499771950764261396/515290591848955905/yt.png"
goo_gl = "https://cdn.discordapp.com/attachments/499771950764261396/515292396679069711/google.png"
gear = "https://cdn.discordapp.com/attachments/499771950764261396/515299978072293405/gear.png"
spark = "https://cdn.discordapp.com/attachments/499771950764261396/515302914240282625/spark.png"
bots = "https://cdn.discordapp.com/attachments/499771950764261396/515323392048627712/bots.png"

@bot.event
async def on_ready():
	servers = list(bot.servers)
#status = f"over {str(len(bot.servers))} servers"
	status = f"for {pref}commands"
	print ("------------------------------------")
	print (f"Bot Name: {bot.user.name}")
	print (f"Bot ID: {bot.user.id}")
	print (f"Discord Version: {discord.__version__}")
	print (f"{botname} is up on {str(len(bot.servers))} servers!")
	print ("Ready when you are master...")
	print ("------------------------------------")
	await bot.change_presence(game=discord.Game(name=status,type=3))
	
##############################################################################################################################
# 🔑 | A D M I N - C O M M A N D S
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member):
	embed = discord.Embed(title="Ban", description = f"{user.mention} has been banned by {ctx.message.author}", color=0xffffff,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	seldel = await bot.say(embed=embed)
	await bot.ban(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.Member):
	embed = discord.Embed(title="Unban", description="{0.name} has been unbanned from the server".format(user), color=0xffffff,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	seldel = await bot.say(embed=embed)
	await bot.unban(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
	embed = discord.Embed(title="Kick", description="**{}** has been kicked from the server".format(user.name), color=0xffffff,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	selfdel = await bot.say(embed=embed)
	await bot.kick(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, msglimit : int):
	deleted = await bot.purge_from(ctx.message.channel, limit=msglimit)
	embed = discord.Embed(title="Clear", description='Cleared **{}** message(s) from the channel'.format(len(deleted)), color=0xffffff,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	selfdel = await bot.say(embed=embed)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
#       embed = discord.Embed(description="Sorry that's too much...", color=0xffafc9,)
#       await bot.say(embed=embed)

#@bot.command(pass_context=True)
#async def ping(ctx):
#	channel = ctx.message.channel
#	t1 = time.perf_counter()
#	await bot.send_typing(channel)
#	t2 = time.perf_counter()
#	await bot.say('Pong! It took {}ms.'.format(round((t2-t1))))
	# Time the time required to send a message first.
	# This is the time taken for the message to be sent, awaited, and then 
	# for discord to send an ACK TCP header back to you to say it has been
	# received; this is dependant on your bot's load (the event loop latency)
	# and generally how shit your computer is, as well as how badly discord
	# is behaving.
	#start = time.monotonic()
	#msg = await bot.say('Pinging...')
	#millis = (time.monotonic() - start) * 1000

	# Since sharded bots will have more than one latency, this will average them if needed.
	#heartbeat = ctx.bot.latency * 1000

	#await msg.edit(content=f'Heartbeat: {heartbeat:,.2f}ms\tACK: {millis:,.2f}ms.')
	
############################
@bot.command(pass_context=True)
async def ms_ping(ctx):
	channel = ctx.message.channel   
	try:
	 t1 = time.perf_counter()
	 await bot.send_typing(channel)
	 ta = t1
	 t2 = time.perf_counter()
	 await bot.send_typing(channel)
	 tb = t2
	 ra = round((tb - ta) * 1000)
	finally:
	 pass
	try:
	 t1a = time.perf_counter()
	 await bot.send_typing(channel)
	 ta1 = t1a
	 t2a = time.perf_counter()
	 await bot.send_typing(channel)
	 tb1 = t2a
	 ra1 = round((tb1 - ta1) * 1000)
	finally:
	 pass
	try:
	 t1b = time.perf_counter()
	 await bot.send_typing(channel)
	 ta2 = t1b
	 t2b = time.perf_counter()
	 await bot.send_typing(channel)
	 tb2 = t2b
	 ra2 = round((tb2 - ta2) * 1000)
	finally:
	 pass
	try:
	 t1c = time.perf_counter()
	 await bot.send_typing(channel)
	 ta3 = t1c

	 t2c = time.perf_counter()
	 await bot.send_typing(channel)
	 tb3 = t2c

	 ra3 = round((tb3 - ta3) * 1000)
	finally:
	 pass
	try:
	 t1d = time.perf_counter()
	 await bot.send_typing(channel)
	 ta4 = t1d

	 t2d = time.perf_counter()
	 await bot.send_typing(channel)
	 tb4 = t2d

	 ra4 = round((tb4 - ta4) * 1000)
	finally:
	 pass

	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Bot Connection", icon_url=dis_cord)
	embed.set_thumbnail(url=vixen)
	embed.add_field(name='Ping 1', value=str(ra), inline=True)
	embed.add_field(name='Ping 2', value=str(ra2), inline=True)
	embed.add_field(name='Ping 3', value=str(ra3), inline=True)
	embed.add_field(name='Ping 4', value=str(ra4), inline=True)
	await bot.say(embed=embed)
############################
@bot.command(pass_context=True)
async def count(ctx):
	bots = 0
	members = 0
	total = 0
	for x in ctx.message.server.members:
	 if x.bot == True:
	  bots += 1
	  total += 1
	 else:
	  members += 1
	  total += 1
	embed = discord.Embed(title="Server Member Count",color=0x7289da)
	embed.set_author(name="Bot Logs", icon_url=warning)
	embed.add_field(name="Bot Count",value=bots)
	embed.add_field(name="Member Count",value=members)
	embed.add_field(name="Total",value=total)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def version(ctx):
	embed = discord.Embed(title="Version", description=f"The current version of {botname} is: `{ver}`", color=0xffffff)
	embed.set_author(name="Bot Logs", icon_url=warning)
	await bot.say(embed=embed)
	
##############################################################################################################################
# 📖 | G E N E R A L - C O M M A N D S
##############################################################################################################################

@bot.command(pass_context=True)
async def prefix(ctx):
	embed = discord.Embed(description=f"{pref}", color=0x7289da)
	embed.set_author(name="Bot Prefix", icon_url=dis_cord)
	await bot.say(embed=embed)
			 
@bot.command(pass_context=True)
async def server(ctx):
	bots = 0
	members = 0
	total = 0
	for x in ctx.message.server.members:
	 if x.bot == True:
	  bots += 1
	  total += 1
	 else:
	  members += 1
	  total += 1
	embed = discord.Embed(description="Here's what I could find.", color=0x7289da)
	embed.set_author(name="Server Info", icon_url=dis_cord)
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	embed.add_field(name="Name:", value=ctx.message.server.name, inline=True)
	embed.add_field(name="ID:", value=ctx.message.server.id, inline=True)
	embed.add_field(name="Region:", value=ctx.message.server.region, inline=True)
	embed.add_field(name="Owner:", value=ctx.message.server.owner.mention, inline=False)
# embed.add_field(name="Varification level:, value=?, inline=True)
	embed.add_field(name="Members:", value=f"Online: {len([I for I in ctx.message.server.members if I.status is discord.Status.online])}\nBots: {bots}\nMembers: {members}\nTotal: {total}", inline=True)
	embed.add_field(name="Roles:", value=len(ctx.message.server.roles), inline=True)
# embed.add_field(name="Channels:", value=?, inline=True)
	embed.add_field(name="Created:", value=ctx.message.server.created_at, inline=False)
# embed.add_field(name="Number of Emotes:", value=?, inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url) 
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def profile(ctx, user: discord.Member):
	embed = discord.Embed(description="Here's what I could find.", color=0x7289da)
	embed.set_author(name="User Info", icon_url=dis_cord)
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="Name", value=user, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=False)
	embed.add_field(name="Highest role", value=user.top_role, inline=False)
	embed.add_field(name="Created", value=user.created_at, inline=True)
	embed.add_field(name="Joined", value=user.joined_at, inline=True)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="User Avatar", icon_url=dis_cord)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name=botname, icon_url=vixen)
	embed.set_thumbnail(url=vixen)
	embed.add_field(name="Prefix", value=f"{pref} | {pref}commands for help", inline=True)
	embed.add_field(name="Creator", value="<@257784039795064833>", inline=True)
	embed.add_field(name="About", value="Hey, this is Vixen a new bot in need of more users.\nShare our bot or join our help server!", inline=True)
	embed.add_field(name="Links", value="<:white:535747728614096906><:vixen:535750323340312576> Website: https://relykxdiscord.wixsite.com/vixen\n\n<:blurple:535747202740518922><:discord:535748146761039872> Help Server: https://discord.gg/UjuGRB9\n\n<:darkorange:535747669872738314><:patreon:535785807584428032> Patreon: https://www.patreon.com/join/vixendiscord?\n\n<:lightorange:535747428893327370><:curiouscat:535750033597923328> Curious Cat: https://curiouscat.me/VixenDiscord\n\n<:lightblue:535747615573147657><:twitter:535749157323931678> Twitter: https://twitter.com/VixenDiscord", inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Invite", icon_url=dis_cord)
	embed.add_field(name="Link:", value="https://discordapp.com/oauth2/authorize?&client_id=496214977267630080&scope=bot&permissions=66186303")
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def vote(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Vote", icon_url=bots)
	embed.add_field(name="Link:", value="https://discordbots.org/bot/496214977267630080/vote")
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def website(ctx):
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name="Website", icon_url=vixen)
	embed.add_field(name="Link:", value="https://relykxdiscord.wixsite.com/mikibot")
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def donate(ctx):
	embed = discord.Embed(description="You can donate here: \nhttps://www.patreon.com/join/vixendiscord?", color=0xf76754)
	embed.set_author(name="Patreon", icon_url=patreon)
	embed.set_thumbnail(url=patreon)
	await bot.say(embed=embed)
	
##############################################################################################################################
# 😜 | F U N - C O M M A N D S													      
##############################################################################################################################
	
@bot.command(pass_context=True)
async def google(ctx,*args):
	x = f"https://www.google.com/search?rlz=1C1CHBF_enUS753US753&ei=n62RW536KpL2swWl1IKIBg&q={args}"
	y = x.replace(" ","+")
	embed = discord.Embed(color=0xf4c20d,)
	embed.set_author(name="Google", icon_url=goo_gl)
	embed.add_field(name="Link:", value=y)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def youtube(ctx,*args):
	x = f"https://www.youtube.com/results?search_query={args}"
	y = x.replace(" ","+")
	embed = discord.Embed(color=0xff0000,)
	embed.set_author(name="YouTube", icon_url=you_be)
	embed.add_field(name="Link:", value=y)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def greet(ctx):
	randomlist = ['Hello',
		      'Hey',
		      'Heyo',
		      'Hello there',
		      'Hey buddy',
		      'Hi',
		      'Nice to meet you',
		      "How's it going",
		      'Heeey',
                     ]
	await bot.say("%s" %(random.choice(randomlist),))

@bot.command(pass_context=True)
async def clock(ctx):
	time = now.strftime("%X")
	date = now.strftime("%x")
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name="Clock", icon_url=clock)
	embed.add_field(name="Time", value=time, inline=True)
	embed.add_field(name="Date", value=date, inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def kawaii(ctx):
	embed = discord.Embed(title="Kawaii Emoji", description="Find more here: https://kawaiiface.net/", color=0xffffff,)
	embed.add_field(name="Happy", value="`(✿◠‿◠)` `≧◡≦` `(▰˘◡˘▰)` `(●´ω｀●)`\n`(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧` `（ミ￣ー￣ミ）` `(づ｡◕‿‿◕｡)づ`\n`✌.ʕʘ‿ʘʔ.✌` `◎[▪‿▪]◎`", inline=False)
	embed.add_field(name="Sad", value="`ಥ_ಥ` `┐(‘～'；)┌` `◄.►` `(◕︵◕)`\n`v( ‘.’ )v` `ਉ_ਉ` `o(╥﹏╥)o` `●︿●` `(∩︵∩)`", inline=False)
	embed.add_field(name="Mad", value="`〴⋋_⋌〵` `(◣_◢)` `☉▵☉凸` `ↁ_ↁ`\n`╚(•⌂•)╝` `ᇂﮌᇂ)` `ლ(́◉◞౪◟◉‵ლ`\n`(┛◉Д◉)┛彡┻━┻ `", inline=False)
	embed.add_field(name="Love", value="`v(=∩_∩=)ﾌ` `(n˘v˘•)¬` `♥╣[-_-]╠♥` `★~(◡﹏◕✿)`\n`(◕‿-)` `( ^▽^)σ)~O~)` `♥‿♥` `(✿ ♥‿♥)` `(●´ω｀●)`", inline=False)
	embed.add_field(name="Party", value="`\m/(>.<)\m/` `ヾ(〃^∇^)ﾉ` `(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧`\n`♨(⋆‿⋆)♨` `┌( ಠ_ಠ)┘` `Ｏ(≧▽≦)Ｏ` `☜-(ΘLΘ)-☞`\n`@(ᵕ.ᵕ)@` `╘[◉﹃◉]╕`", inline=False)
	embed.add_field(name="Weird", value="`（ ´_⊃｀）` `(￣。￣)～ｚｚｚ` `~(⊕⌢⊕)~` `⊂•⊃_⊂•⊃`\n`ᕙ(⇀‸↼‶)ᕗ` `( 　ﾟ,_ゝﾟ)` `(⊙︿⊙✿)`\n`̿̿’̿’\̵͇̿̿\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿` `( ͡° ͜ʖ ͡°)`", inline=False)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def cat(ctx):
	r = requests.get('https://api.thecatapi.com/v1/images/search').json()
	url = (r[0]['url'])
	embed = discord.Embed(description="Here's a cute kitten :D", color=0xffffff,)
	embed.set_image(url=url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def dog(ctx):
	r = requests.get('https://api.thedogapi.com/v1/images/search').json()
	url = r[0]['url']
	embed = discord.Embed(description="Here's a cute doggie :D", color=0xffffff)
	embed.set_image(url=url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def wallpaper(ctx):
	embed = discord.Embed(color=0xffffff,)
	embed.set_image(url='https://picsum.photos/1280/720/?image=' + str(random.randint(1, 999)))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def gif(ctx):
	embed = discord.Embed(color=0xffffff,)
	embed.set_image(url='http://replygif.net/i/' + str(random.randint(90, 1100)) + '.gif')
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def password(ctx):
	embed = discord.Embed(title=f"{botname} Commands", description=":mailbox_with_mail: Check DMs", color=0xffffff)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url)
	await bot.say(embed=embed)
	encryptkey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
	encryptcode = ['1','2','3','4','5','6','7','8','9',]
	count1 = random.randint(1, 52)
	count2 = random.randint(1, 52)
	count3 = random.randint(1, 52)
	count4 = random.randint(1, 52)
	count5 = random.randint(1, 52)
	count6 = random.randint(1, 52)
	count7 = random.randint(1, 52)
	count8 = random.randint(1, 52)
	count9 = random.randint(1, 52)
	count10 = random.randint(1, 52)
	count11 = random.randint(1, 52)
	count12 = random.randint(1, 52)
	count13 = random.randint(1, 52)
	count14 = random.randint(1, 52)
	count15 = random.randint(1, 52)
	count16 = random.randint(1, 52)
	if count1 < 26:
	 key1 = (random.choice(encryptkey))
	if count1 >= 26: 
	 key1 = (random.choice(encryptcode))
	if count2 < 26:
	 key2 = (random.choice(encryptkey))
	if count2 >= 26: 
	 key2 = (random.choice(encryptcode))
	if count3 < 26:
	 key3 = (random.choice(encryptkey))
	if count3 >= 26: 
	 key3 = (random.choice(encryptcode))
	if count4 < 26:
	 key4 = (random.choice(encryptkey))
	if count4 >= 26: 
	 key4 = (random.choice(encryptcode))
	if count5 < 26:
	 key5 = (random.choice(encryptkey))
	if count5 >= 26: 
	 key5 = (random.choice(encryptcode))
	if count6 < 26:
	 key6 = (random.choice(encryptkey))
	if count6 >= 26: 
	 key6 = (random.choice(encryptcode))
	if count7 < 26:
	 key7 = (random.choice(encryptkey))
	if count7 >= 26: 
	 key7 = (random.choice(encryptcode))
	if count8 < 26:
	 key8 = (random.choice(encryptkey))
	if count8 >= 26: 
	 key8 = (random.choice(encryptcode))
	if count9 < 26: 
	 key9 = (random.choice(encryptkey))
	if count9 >= 26: 
	 key9 = (random.choice(encryptcode))
	if count10 < 26: 
	 key10 = (random.choice(encryptkey))
	if count10 >= 26: 
	 key10 = (random.choice(encryptcode))
	if count11 < 26: 
	 key11 = (random.choice(encryptkey))
	if count11 >= 26: 
	 key11 = (random.choice(encryptcode))
	if count12 < 26:
	 key12 = (random.choice(encryptkey))
	if count12 >= 26:
	 key12 = (random.choice(encryptcode))
	if count13 < 26:
	 key13 = (random.choice(encryptkey))
	if count13 >= 26:
	 key13 = (random.choice(encryptcode))
	if count14 < 26:
	 key14 = (random.choice(encryptkey))
	if count14 >= 26:
	 key14 = (random.choice(encryptcode))
	if count15 < 26:
	 key15 = (random.choice(encryptkey))
	if count15 >= 26:
	 key15 = (random.choice(encryptcode))
	if count16 < 26:
	 key16 = (random.choice(encryptkey))
	if count16 >= 26:
	 key16 = (random.choice(encryptcode))
# There are about ???,???,??? different password combinations that can be generated.
	encryptedpass = (key1 + key2 + key3 + key4 + key5 + key6 + key7 + key8 + key9 + key10 + key11 + key12 + key13 + key14 + key15 + key16)
	embed = discord.Embed(description='Here is your randomly generated password: ' + '`' + encryptedpass + '`', color=0xffffff)
	await bot.send_message(ctx.message.author, embed=embed)
	
##############################################################################################################################
# 👾 | G A M E - C O M M A N D S	
##############################################################################################################################

@bot.command(pass_context=True)
async def diceroll(ctx):
	randomlist = ['1','2','3','4','5','6',]
	embed = discord.Embed(title ="Dice Roll", description="*rolls a dice*", color=0xffffff,)
	embed.add_field(name="You rolled a dice and it landed on...", value="Side: **%s**" %(random.choice(randomlist),))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def coinflip(ctx):
	randomlist = ['Heads','Tails',]
	embed = discord.Embed(title ="Coin Flip", description="*flips a coin*", color=0xffffff,)
	embed.add_field(name="You flipped a coin and it landed on", value="Face: **%s**" %(random.choice(randomlist),))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def eightball(ctx):
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
	embed = discord.Embed(title ="8 Ball", description="*shakes the 8 Ball up...*", color=0xffffff,)
	embed.add_field(name="You shook the 8 ball and it shows you...", value="Answer: **%s**" %(random.choice(randomlist),))
	await bot.say(embed=embed)

##############################################################################################################################
# 🛠️ | O W N E R - C O M M A N D S	
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def servercount(ctx):
	embed = discord.Embed(description=f"Currently watching over {str(len(bot.servers))} Discord servers", color=0x7289da)
	embed.set_author(name="Server Count", icon_url=dis_cord)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def serverlist(ctx):
	embed = discord.Embed(title="Server List", color=0x7289da)
	embed.set_author(name="Bot Logs", icon_url=warning)
	await bot.say(embed=embed)
	serv = list(bot.servers)
	embed = discord.Embed(description=f"Currently watching over {str(len(bot.servers))} Discord servers", color=0x7289da)
	embed.set_author(name="Server List", icon_url=dis_cord)
	await bot.say(embed=embed)
	for x in range(len(serv)):
	 embed = discord.Embed(color=0x7289da,)
	 embed.set_thumbnail(url=serv[x-1].icon_url)
	 embed.add_field(name="Name:", value=serv[x-1].name, inline=False)
	 embed.add_field(name="ID:", value=serv[x-1].id, inline=False)
	 embed.add_field(name="Region:", value=serv[x-1].region, inline=True)
	 embed.add_field(name="Owner:", value=serv[x-1].owner, inline=False)
	 embed.add_field(name="Members:", value=len(serv[x-1].members), inline=True)
	 embed.add_field(name="Roles:", value=len(serv[x-1].roles), inline=True)
	 embed.add_field(name="Created:", value=serv[x-1].created_at, inline=False)
	 await bot.say(embed=embed)
	
##############################################################################################################################
# 🚫 | T E S T I N G - C O M M A N D S
##############################################################################################################################

#@bot.command(pass_context=True)
#async def ping(ctx):
#	channel = ctx.message.channel
#	t1 = time.perf_counter()
#	await bot.send_typing(channel)
#	t2 = time.perf_counter()
#	await bot.say('Pong! It took {}ms.'.format(round((t2-t1))))

##############################################################################################################################
# ℹ️ | H E L P - C O M M A N D S	
##############################################################################################################################

@bot.command(pass_context=True)
async def commands(ctx):
	embed = discord.Embed(title=f"{botname} Commands", description=":mailbox_with_mail: Check DMs", color=0xffffff)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url)
	await bot.say(embed=embed)
	embed = discord.Embed(title=f"{botname} Commands", description="idk yet", color=0xffffff)
	await bot.send_message(ctx.message.author, embed=embed)
	embed = discord.Embed(description="All commands for Admin:", color=0xffffff)
	embed.set_author(name="Admin", icon_url=warning)
	embed.add_field(name="ban", value="Bans the mentioned user", inline=False)
	embed.add_field(name="unban", value="Unbans the mentioned user", inline=False)
	embed.add_field(name="kick", value="Kicks the mentioned user", inline=False)
	embed.add_field(name="clear", value="Clears a specific amount of messages in a channel", inline=False)
	embed.add_field(name="ping", value=f"Displays current ping of {botname}", inline=False)
	embed.add_field(name="count", value="Displays the amount of members in the current server", inline=False)
	embed.add_field(name="version", value=f"Displays the current version of {botname}", inline=False)
	await bot.send_message(ctx.message.author, embed=embed)
	embed = discord.Embed(description="All commands for General:", color=0xffffff)
	embed.set_author(name="General", icon_url=gear)
	embed.add_field(name="prefix", value="Displays the current prefix", inline=False)
	embed.add_field(name="server", value="Displays the info of the current server", inline=False)
	embed.add_field(name="user", value="Displays a profile of the mentioned user", inline=False)
	embed.add_field(name="avatar", value="Displays the profile pic of the mentioned user", inline=False)
	embed.add_field(name="about", value=f"Displays the About description of {botname}", inline=False)
	embed.add_field(name="invite", value=f"Sends the invite link to add {botname} to your server", inline=False)
	embed.add_field(name="vote", value=f"Sends the voting link for {botname}", inline=False)
	embed.add_field(name="donate", value=f"Sends the donate link for {botname}", inline=False)
	await bot.send_message(ctx.message.author, embed=embed)
	embed = discord.Embed(description="All commands for Fun:", color=0xffffff)
	embed.set_author(name="Fun", icon_url=spark)
	embed.add_field(name="google", value="Googles your search", inline=False)
	embed.add_field(name="youtube", value="Searches for the most relevant youtube video", inline=False)
	embed.add_field(name="greet", value="Generates a greeting response", inline=False)
	embed.add_field(name="password", value="Generates a random password", inline=False)
	embed.add_field(name="time", value="Displays the current time of the server", inline=False)
	embed.add_field(name="kawaii", value="Displays multiple different kawaii emoji", inline=False)
	embed.add_field(name="cat", value="Generates a random cat pic", inline=False)
	embed.add_field(name="dog", value="Generates a random dog pic", inline=False)
	embed.add_field(name="wallpaper", value="Generates a random wallpaper", inline=False)
	embed.add_field(name="gif", value="Generates a random gif", inline=False)
	embed.add_field(name="diceroll", value="Rolls a six sided die", inline=False)
	embed.add_field(name="coinflip", value="Flips a coin, could be heads could be tails", inline=False)
	embed.add_field(name="eightball", value="Ask a question and shake the 8 Ball", inline=False)
	await bot.send_message(ctx.message.author, embed=embed)
	
bot.run(os.getenv("BOT_TOKEN"))
