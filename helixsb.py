import discord
import logging 
from discord.ext import commands
import random
import os
from bs4 import BeautifulSoup
import time
from discord.ext import commands, tasks
from colorama import init, Fore
from pystyle import Center, Colorate, Colors
import asyncio
import requests 
import datetime
from faker import Faker
import random
import base64
from datetime import datetime
from pypresence import Presence




TOKEN = input("[/] ENTER YOUR BOT TOKEN : ") .strip()

intents=discord.Intents.default()

command_prefix = '>'


bot = commands.Bot(command_prefix=command_prefix,intents=intents, self_bot=True, guild_subscriptions=False, guild_scraping=False)


afk_status = False
afk_start_time = None
afk_user = None
mention_message_sent = False


recent_message = None

init()

def get_console_width():
    try:
        columns, _ = os.get_terminal_size(0)
    except OSError:
        columns, _ = os.get_terminal_size(1)
    return columns

def print_centered_text(text, color):
    
    console_width = get_console_width()
    separator = "═"  
    padding = (console_width - len(text)) // 2

    
print(Colorate.Horizontal(Colors.blue_to_red,
Center.XCenter("""       ___     
   / / / /__  / (_)  __
  / /_/ / _ \/ / / |/_/
 / __  /  __/ / />  <  
/_/ /_/\___/_/_/_/|_|  
                       
   _____      ________          __ 
  / ___/___  / / __/ /_  ____  / /_
  \__ \/ _ \/ / /_/ __ \/ __ \/ __/
 ___/ /  __/ / __/ /_/ / /_/ / /_  
/____/\___/_/_/ /_.___/\____/\__/  """)))
print(Colorate.Horizontal(Colors.cyan_to_blue, Center.XCenter("\ndeveloped by mercury#0007\n")))
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter("════════════════════════════════════════")))
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter("════════════════════════════════════════")))


    
console_width = get_console_width()

    
options_text = (f'''𝐈𝐍𝐅𝐎:\n[+] Version:- 2.7.4\n[+] logged in as :{bot.user}\n[+] Categories available: 4 \n[+] commands available : 𝟐𝟒 \n[+] client id :\n[+] Status :Online''')
separator_padding = (console_width - len(options_text)) // 2
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(options_text)))
print(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter("════════════════════════════════════════")))
print(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter("════════════════════════════════════════")))
def clear():
  os.system('clear')
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Set the streaming activity
    streaming = discord.Streaming(
        name='nooking random kids',
        url='https://twitch.tv/twitch'
    )
    
    

@bot.command(help="Ping-pong!")
async def ping(ctx):
  await ctx.reply('pong!')
  
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    owner = guild.owner
    member_count = guild.member_count
    bot_count = len([member for member in guild.members if member.bot])
    human_count = member_count - bot_count
    emoji_count = len(guild.emojis)
    role_count = len(guild.roles)
    channel_count = len(guild.channels)
    created_at = guild.created_at.strftime("%Y-%m-%d %H:%M:%S GMT")
    
    info = (
        f"**Server Information for {guild.name}**\n"
        f"```\n"
        f"Owner: {owner}\n"
        f"Member Count: {member_count}\n"
        f"Human Members: {human_count}\n"
        f"Bot Members: {bot_count}\n"
        f"Emoji Count: {emoji_count}\n"
        f"Role Count: {role_count}\n"
        f"Channel Count: {channel_count}\n"
        f"Created On: {created_at}\n"
        f"Server ID: {guild.id}\n"
        f"```"
    )

    await ctx.send(info)
    


 


common_words = ["hi", "hello", "yo"] 

fake = Faker()

@bot.command()
async def fdoggs(ctx, user: discord.Member):
   
    fake_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    fake_city = fake.city()
    fake_zip = str(random.randint(10000, 99999))
    fake_state = fake.state()
    fake_country = fake.country()

 
 
    user_id = user.id
    username = user.name
    half_token = base64.b64encode(str(user_id).encode()).decode()[:10]

 
    fake_info_message = f"```Username: {username}\nIP: {fake_ip}\nCity: {fake_city}\nState: {fake_state}\nCountry: {fake_country}\nZip: {fake_zip}\nUser ID: {user_id}\nHalf user token: {half_token}```"

    await ctx.send(fake_info_message)
@bot.command()
async def play(ctx, *, game_name):
    await bot.change_presence(activity=discord.Game(name=game_name))
    await ctx.send(f'Changed activity to Playing {game_name}')

@bot.command()
async def listen(ctx, *, activity_name):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_name))
    await ctx.send(f'Changed activity to Listening to {activity_name}')

@bot.command()
async def watch(ctx, *, activity_name):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity_name))
    await ctx.send(f'Changed activity to Watching {activity_name}')

@bot.command()
async def stream(ctx, *, args):
    args_list = args.split(',')
    if len(args_list) != 2:
        await ctx.send("Please provide both the name and the URL for streaming.")
        return

    name, url = args_list
    await bot.change_presence(activity=discord.Streaming(name=name.strip(), url=url.strip()))
    await ctx.send(f'Changed activity to Streaming {name}')
    



afk_status = False
afk_user = None

@bot.command()
async def alertson(ctx):
    global afk_status, afk_user
    afk_status = True
    afk_user = ctx.author 
    await ctx.send("AFK alerts are now enabled.")

@bot.command()
async def alertsoff(ctx):
    global afk_status, afk_user
    afk_status = False
    afk_user = None
    await ctx.send("AFK alerts are now disabled.")

@bot.event
async def on_message(message):
    global afk_status, afk_user
    if afk_status and message.author != bot.user and afk_user and afk_user.mentioned_in(message):
        await message.channel.send(f"{message.author.mention}, the pinged user is AFK! - sent by the bot")
    
    await bot.process_commands(message)









    

@bot.command()
async def gaymeter(ctx, member: discord.Member):
    gay_percentage = random.randint(0, 100)
    await ctx.send(f"{member.mention} is {gay_percentage}% gay!")


deleted_messages = {}


edited_messages = {}

@bot.event
async def on_message_delete(message):
    deleted_messages[message.channel.id] = (message.author, message.content)

@bot.event
async def on_message_edit(before, after):
    edited_messages[before.channel.id] = (before.author, before.content, after.content)

@bot.command(name='snipe')
async def snipe(ctx):
    channel = ctx.channel
    try:
        author_deleted, content_deleted = deleted_messages.get(channel.id, (None, None))
        author_edited, before_content, after_content = edited_messages.get(channel.id, (None, None, None))

        snipe_message_deleted = f"Last deleted message in #{channel.name}:\n{content_deleted}\n\nThis message was sent by {author_deleted}" if author_deleted else "No recently deleted messages in this channel"
        snipe_message_edited = f"Last edited message in #{channel.name}:\nBefore: {before_content}\nAfter: {after_content}\n\nThis message was sent by {author_edited}" if author_edited else "No recently edited messages in this channel"

        await ctx.send(snipe_message_deleted)
        await ctx.send(snipe_message_edited)
        
    except KeyError:
        await ctx.send(f"No recently deleted or edited messages in #{channel.name}")


            
@bot.command(help="Clears the chat.")
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send("\u3164" * 600 + "**cleared successfully!**")

@bot.command(help="Purge messages from the channel.")
async def purge(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Purged {amount} messages.")
    else:
        await ctx.send("You don't have permission to purge messages.")

@bot.command(help="Kicks a member from the server.")
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked.")
    else:
        await ctx.send("You don't have permission to kick members.")

@bot.command(help="Bans a member from the server.")
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned.")
    else:
        await ctx.send("You don't have permission to ban members.")

@bot.command(help="Unbans a member from the server.")
async def unban(ctx, *, member):
    if ctx.author.guild_permissions.ban_members:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}.")
                return

        await ctx.send("User not found in the ban list.")
    else:
        await ctx.send("You don't have permission to unban members.")

@bot.command(help="Set AFK status on/off.")
async def afk(ctx, status: str = "on"):
    global afk_status
    if status == "on":
        afk_status = True
        await ctx.send("AFK status is now enabled.")
    elif status == "off":
        afk_status = False
        await ctx.send("AFK status is now disabled.")
    else:
        await ctx.send("Invalid usage. Use '>afk on' to enable and '>afk off' to disable.")
@bot.command()
async def commands(ctx):
    
    categories = {
        "Fun": {
            "gaymeter": "Check someone's gay percentage.",
            "sop": "smash or pass!.",
            "clear": "clears the chat!",
            "lm": "Shows love meter between two users.",
            "fdoggs": "doggs the mentioned user",
            "s": "starts spamming [message]!",
            "st": "stops the spam",
            "ping60": "pings random users",
            "stop": "stops pinging random users for the ping60 command.",
        },
        "Moderation": {
            "purge": "Purge messages from the channel.",
            "kick": "Kick a member from the server.",
            "ban": "Ban a member from the server.",
            "unban": "Unban a member from the server.",
        },
        "Miscellaneous": {
            "ping": "Ping-pong!",
            "alertson": "Enables AFK alerts.",
            "alertsoff": "Disables AFK alerts.",
            "snipe": "Display the most recently edited/deleted message.",
            "whois": "Retrieve IP information.",
            "Prefix": "shows you the current prefix.",
        },
        "Activities": {
            "play": "Set your activity type to playing! (name).",
            "stream": "Set your activity type to streaming! {name,url(recommended to set it to https://twitch.tv/), and after entering name, separate the link by giving a comma.",
            "watch": "Set your activity type to watching! (name).",
            "listen": "Set your activity type to listening!(name)."
        }
    }

    
    help_msg = "```Available commands:\n"

    for category, commands in categories.items():
        help_msg += f"{category}:\n"
        for command, usage in commands.items():
            help_msg += f">{command} - {usage}\n"
        help_msg += "\n"

    help_msg += "```"

    await ctx.send(help_msg)
    


pinging = False  



@bot.command()
async def ping60(ctx):
    global pinging
    if not pinging:
        pinging = True
        while pinging:
           
            members = random.sample(ctx.guild.members, int(len(ctx.guild.members) * 0.6))

            
            mentions = [member.mention for member in members]

            
            ping_message = ' '.join(mentions)

            
            ping_msg = await ctx.send(ping_message)
            await asyncio.sleep(2)
            await ping_msg.delete()
    else:
        await ctx.send("Pinging process is already active. Use >stop to stop it.")

@bot.command()
async def stop(ctx):
    global pinging
    if pinging:
        pinging = False
        await ctx.send('Pinging process stopped.')
    else:
        await ctx.send('Pinging process is not active.')
@bot.command()
async def prefix(ctx):
  await ctx.reply(f'my preix is `{command_prefix}`.')
 
repeating_messages = {}
@bot.command()
async def s(ctx, *, message):
    if ctx.channel.id not in repeating_messages:
        repeating_messages[ctx.channel.id] = message
        await ctx.send(f"Repeating '{message}' every 2 seconds.")
        await repeat_message(ctx.channel)
    else:
        await ctx.send("A message is already being repeated in this channel!")

@bot.command()
async def st(ctx):
    if ctx.channel.id in repeating_messages:
        del repeating_messages[ctx.channel.id]
        await ctx.send("Stopped repeating the message.")

async def repeat_message(channel):
    while channel.id in repeating_messages:
        await channel.send(repeating_messages[channel.id])
        

@bot.command()
async def whois(ctx, ip):
    # Call the ipinfo.io API
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        city = data.get("city", "N/A")
        country = data.get("country", "N/A")
        timezone = data.get("timezone", "N/A")
        postal_code = data.get("postal", "N/A")
        location = data.get("loc", "N/A").split(',')
        latitude = location[0]
        longitude = location[1]

        await ctx.send(f"```IP: {ip}\nCity: {city}\nCountry: {country}\nTimezone: {timezone}\nPostal Code: {postal_code}\nLongitude: {longitude}\nLatitude:{latitude}```")
    else:
        await ctx.send("Unable to fetch IP information.")

sop = [
    "https://wallpapercave.com/wp/wp6553618.jpg",
    'https://cdn.weeb.sh/images/rJxH-30OPZ.jpeg',
    'https://i.pinimg.com/originals/ec/27/ac/ec27ac45ffa4b2d09d6d06038f052c4c.jpg',
    'https://cdn.weeb.sh/images/HJoRMOcNM.jpeg',
    'https://wallpaperaccess.com/full/45931.jpg',
    'https://w7.pngwing.com/pngs/176/930/png-transparent-catgirl-anime-anime-mammal-cat-like-mammal-carnivoran-thumbnail.png',
    'https://qph.cf2.quoracdn.net/main-qimg-2d8ba8cb4941c6f156e47f1c69553350-lq',
    'https://i.pinimg.com/originals/a7/a8/a8/a7a8a82a01655df948ece40fd1bfb2d9.jpg',
    'https://w0.peakpx.com/wallpaper/357/333/HD-wallpaper-anime-girls-blush-simple-background-animal-ears-sitting-tail-animal-tail-cat-ears-cat-girl-cat-tail-anime-thumbnail.jpg',
    'https://simg.nicepng.com/png/small/298-2984541_report-abuse-hinh-anime-cat-girl.png',
    'https://w0.peakpx.com/wallpaper/853/379/HD-wallpaper-anime-anime-girls-cat-girl-amashiro-natsuki-nacho-neko-animal-ears-grey-hair-aqua-eyes-chocolate-thumbnail.jpg',
    'https://static.boredpanda.com/blog/wp-content/uploads/2021/06/The-Japanese-artist-imagined-what-cats-would-be-like-if-they-were-manga-style-girls-6-Pics-60d973f338f90__880.jpg',
  'https://www.deviantart.com/hyanna-natsu/art/Fanart-Marin-Kitagawa-906900788',
  'https://www.deviantart.com/rosuuri/art/Myu-683833784',
  
]


@bot.command(name='sop')
async def smash_or_pass(ctx):
    random_image_url = random.choice(sop)

    
    message = f'Smash or Pass?\n{random_image_url}'
    await ctx.send(message)

@bot.command()
async def lm(ctx, user1: discord.Member, user2: discord.Member):
    
    love_percentage = random.randint(0, 100)

    
    await ctx.send(f"{user1.mention} ❤️ {user2.mention}\nLove Percentage: {love_percentage}%")

bot.run(TOKEN, bot=False) # Go to line 21 and enter your token as clarified

# Enjoy Helix selfbot! developed by Mercury with love! 
