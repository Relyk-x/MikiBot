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
import bs4, requests
import time
import os

bot = commands.Bot(command_prefix='v!')
msglimit = 100
now = datetime.now()
ver = "v0.5.4"#1
botname = "Vixen"

#Emoji
vixen = "https://cdn.discordapp.com/attachments/499771950764261396/515112832342425610/botpic.png"
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
	status = f"over {str(len(bot.servers))} servers"
	print (f"Bot Name: {bot.user.name}")
	print (f"Bot ID: {bot.user.id}")
	print (f"{botname} is up on {str(len(bot.servers))} servers!")
	print ("Ready when you are...")
	await bot.change_presence(game=discord.Game(name=status,type=3))
	
@bot.event
async def on_member_join(member):
	print('Sent message to ' + member.name)
	servers = list(bot.servers)
	print(f"Connected on {str(len(bot.servers))} servers:")
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name=botname, icon_url=vixen)
	embed.set_thumbnail(url=vixen)
	embed.add_field(name="Prefix", value="v! | v!commands for help", inline=True)
	embed.add_field(name="Creator", value="<@257784039795064833>", inline=True)
	embed.add_field(name="About", value="Hey, this is Vixen a new bot in need of more users.\nShare our bot or join our help server!", inline=True)
	embed.set_footer(text=f"version: {ver}",)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name="Website", icon_url=vixen)
	embed.add_field(name="Link:", value="https://relykxdiscord.wixsite.com/vixen", inline=False)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Server", icon_url=dis_cord)
	embed.add_field(name="Link:", value="https://discord.gg/UjuGRB9", inline=False)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0xce7a1e,)
	embed.set_author(name="Curious Cat", icon_url=curiouscat)
	embed.add_field(name="Link:", value="https://curiouscat.me/VixenDiscord", inline=False)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0x2da9e1,)
	embed.set_author(name="Twitter", icon_url=twitter)
	embed.add_field(name="Link:", value="https://twitter.com/VixenDiscord", inline=False)
	await bot.send_message(member, embed=embed)

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
# embed = discord.Embed(description="Sorry that's too much...", color=0xffafc9,)
# await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
	embed = discord.Embed(title="Ping", description=":construction:  under construction :construction:", color=0xffffff)
	embed.set_author(name="Bot Logs", icon_url=warning)
	await bot.say(embed=embed)
	# Time the time required to send a message first.
	# This is the time taken for the message to be sent, awaited, and then 
	# for discord to send an ACK TCP header back to you to say it has been
	# received; this is dependant on your bot's load (the event loop latency)
	# and generally how shit your computer is, as well as how badly discord
	# is behaving.
#	start = time.monotonic()
#	msg = await ctx.send('Pinging...')
#	millis = (time.monotonic() - start) * 1000

	# Since sharded bots will have more than one latency, this will average them if needed.
#	heartbeat = ctx.bot.latency * 1000

#	await msg.edit(content=f'Heartbeat: {heartbeat:,.2f}ms\tACK: {millis:,.2f}ms.')
	
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
	embed = discord.Embed(title="Server Member Count",color=0xffffff)
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
	embed = discord.Embed(description="v!", color=0xffffff)
	embed.set_author(name="Prefix", icon_url=dis_cord)
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
	embed = discord.Embed(description="Here's what I could find.", color=0xffffff)
	embed.set_author(name="Server Info", icon_url=dis_cord)
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	embed.add_field(name="Name:", value=ctx.message.server.name, inline=True)
	embed.add_field(name="ID:", value=ctx.message.server.id, inline=True)
	embed.add_field(name="Region:", value=ctx.message.server.region, inline=True)
	embed.add_field(name="Owner:", value=ctx.message.server.owner.mention, inline=True)
# embed.add_field(name="Varification level:, value=?, inline=True)
	embed.add_field(name="Members:", value=f"Online: {len([I for I in ctx.message.server.members if I.status is discord.Status.online])}\nBots: {bots}\nMembers: {members}\nTotal: {total}", inline=True)
	embed.add_field(name="Roles:", value=len(ctx.message.server.roles), inline=True)
# embed.add_field(name="Channels:", value=?, inline=True)
	embed.add_field(name="Created:", value=ctx.message.server.created_at, inline=False)
# embed.add_field(name="Number of Emotes:", value=?, inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url) 
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def user(ctx, user: discord.Member):
	embed = discord.Embed(description="Here's what I could find.", color=0xffffff)
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
	embed = discord.Embed(description=f"Here it is {user.name}'s profile pic",color=0xffffff)
	embed.set_author(name="User Avatar", icon_url=dis_cord)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name=botname, icon_url=vixen)
	embed.set_thumbnail(url=vixen)
	embed.add_field(name="Prefix", value="v! | v!commands for help", inline=True)
	embed.add_field(name="Creator", value="<@257784039795064833>", inline=True)
	embed.add_field(name="About", value="Hey, this is Vixen a new bot in need of more users.\nShare our bot or join our help server!", inline=True)
	embed.set_footer(text=f"version: {ver}",)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name="Website", icon_url=vixen)
	embed.add_field(name="Link:", value="https://relykxdiscord.wixsite.com/vixen", inline=False)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Server", icon_url=dis_cord)
	embed.add_field(name="Link:", value="https://discord.gg/UjuGRB9", inline=False)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0xce7a1e,)
	embed.set_author(name="Curious Cat", icon_url=curiouscat)
	embed.add_field(name="Link:", value="https://curiouscat.me/VixenDiscord", inline=False)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0x2da9e1,)
	embed.set_author(name="Twitter", icon_url=twitter)
	embed.add_field(name="Link:", value="https://twitter.com/VixenDiscord", inline=False)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name="Invite", icon_url=dis_cord)
	embed.add_field(name="Link:", value="https://discordapp.com/oauth2/authorize?&client_id=496214977267630080&scope=bot&permissions=66186303")
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def vote(ctx):
	embed = discord.Embed(color=0xffffff,)
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
async def time(ctx):
	time = now.strftime("%X")
	date = now.strftime("%x")
	embed = discord.Embed(color=0xffffff,)
	embed.set_author(name="Clock", icon_url=clock)
	embed.add_field(name="Time", value=time, inline=True)
	embed.add_field(name="Date", value=date, inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url) 
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
async def servercount(ctx):
	embed = discord.Embed(description=f"Currently watching over {str(len(bot.servers))} Discord servers", color=0xffffff)
	embed.set_author(name="Server Count", icon_url=dis_cord)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def serverlist(ctx):
	serv = list(bot.servers)
	embed = discord.Embed(title="Server List", description=f"Currently watching over {str(len(bot.servers))} Discord servers", color=0x7289da)
	embed.set_author(name="Server List", icon_url=dis_cord)
	for x in range(len(serv)):
	 embed.add_field(name=serv[x-1].name, value=f"● ServerID: {serv[x-1].id}", inline=True)
	 await asyncio.sleep(30)
         await bot.say(embed=embed)
	
##############################################################################################################################
# 🚫 | R E M O V E D - C O M M A N D S
##############################################################################################################################


##############################################################################################################################
# ℹ️ | H E L P - C O M M A N D S	
##############################################################################################################################

@bot.command(pass_context=True)
async def commands(ctx):
	embed = discord.Embed(description="All commands under the Admin categorie:", color=0xffffff)
	embed.set_author(name="Admin", icon_url=warning)
	embed.add_field(name="ban", value="Bans the mentioned user", inline=False)
	embed.add_field(name="unban", value="Unbans the mentioned user", inline=False)
	embed.add_field(name="kick", value="Kicks the mentioned user", inline=False)
	embed.add_field(name="clear", value="Clears a specific amount of messages in a channel", inline=False)
	embed.add_field(name="ping", value=f"Displays current ping of {botname}", inline=False)
	embed.add_field(name="count", value="Displays the amount of members in the current server", inline=False)
	embed.add_field(name="version", value=f"Displays the current version of {botname}", inline=False)
	await bot.say(embed=embed)
	embed = discord.Embed(description="All commands under the General categorie:", color=0xffffff)
	embed.set_author(name="General", icon_url=gear)
	embed.add_field(name="prefix", value="Displays the current prefix", inline=False)
	embed.add_field(name="server", value="Displays the info of the current server", inline=False)
	embed.add_field(name="user", value="Displays a profile of the mentioned user", inline=False)
	embed.add_field(name="avatar", value="Displays the profile pic of the mentioned user", inline=False)
	embed.add_field(name="about", value=f"Displays the About description of {botname}", inline=False)
	embed.add_field(name="invite", value=f"Sends the invite link to add {botname} to your server", inline=False)
	embed.add_field(name="vote", value=f"Sends the voting link for {botname}", inline=False)
	embed.add_field(name="donate", value=f"Sends the donate link for {botname}", inline=False)
	await bot.say(embed=embed)
	embed = discord.Embed(description="All commands under the Fun categorie:", color=0xffffff)
	embed.set_author(name="Fun", icon_url=spark)
	embed.add_field(name="google", value="Googles your search", inline=False)
	embed.add_field(name="youtube", value="Searches for the most relevant youtube video", inline=False)
	embed.add_field(name="greet", value="Generates a greeting response", inline=False)
	embed.add_field(name="time", value="Displays the current time of the server", inline=False)
	embed.add_field(name="kawaii", value="Displays multiple different kawaii emoji", inline=False)
	embed.add_field(name="cat", value="Generates a random cat pic", inline=False)
	embed.add_field(name="dog", value="Generates a random dog pic", inline=False)
	embed.add_field(name="wallpaper", value="Generates a random wallpaper", inline=False)
	embed.add_field(name="gif", value="Generates a random gif", inline=False)
	embed.add_field(name="diceroll", value="Rolls a six sided die", inline=False)
	embed.add_field(name="coinflip", value="Flips a coin, could be heads could be tails", inline=False)
	embed.add_field(name="eightball", value="Ask a question and shake the 8 Ball", inline=False)
	await bot.say(embed=embed)
	
bot.run(os.getenv("BOT_TOKEN"))
