import discord, os, keep_alive, asyncio, datetime, pytz, requests
from discord.ext import tasks, commands
from asyncio import sleep

client = commands.Bot(
  command_prefix=':',
  status=discord.Status.online,
  self_bot=True
)

async def on_ready():
    client.remove_command('help')


async def status_task():
    while True:
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="last.fm"))
        #await client.change_presence(activity = discord.Streaming(name = "BEDWARS Hypixel", url = "https://www.twitch.tv/wallibear"))
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="last.fm/music"))
        #await client.change_presence(activity = discord.Streaming(name = "last.fm", url = "https://www.twitch.tv/"))
        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🥶'))
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='👀'))
        await asyncio.sleep(10)   

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online,activity=discord.CustomActivity(name='Custom status' ,emoji='🍩'))
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='☄️'))
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🤯'))
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🏝'))
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🚀'))
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Phasmophobia", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='📈'))
        await asyncio.sleep(10)     

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3)         

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🌪')) 
        await asyncio.sleep(10)     

        await client.change_presence(activity = discord.Streaming(name = "Among Us", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3)         

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🍇')) 
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🤏')) 
        await asyncio.sleep(10)  

        await client.change_presence(activity = discord.Streaming(name = "Rainbow Six Seige", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3)         

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='💔')) 
        await asyncio.sleep(10)  

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='💯')) 
        await asyncio.sleep(10)  

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🏜')) 
        await asyncio.sleep(10)    

        await client.change_presence(activity = discord.Streaming(name = "Dead By Daylight", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3)         

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='👿')) 
        await asyncio.sleep(10)

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🗣')) 
        await asyncio.sleep(10)   

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3)         

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='👽')) 
        await asyncio.sleep(10)  

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🤳')) 
        await asyncio.sleep(10)  

        await client.change_presence(activity = discord.Streaming(name = "Just Chatting", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🤡')) 
        await asyncio.sleep(10)  

        await client.change_presence(activity = discord.Streaming(name = "NETFLIX", url = "https://www.twitch.tv/sarayaofficial"))
        await asyncio.sleep(3) 

        await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom status' ,emoji='🕯')) 
        await asyncio.sleep(10)                                                                             
        
@client.event
async def on_connect():
  client.loop.create_task(status_task())
  #await client.change_presence(activity = discord.Streaming(name = "BEDWARS Hypixel", url = "https://www.twitch.tv/wallibear"))
keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)