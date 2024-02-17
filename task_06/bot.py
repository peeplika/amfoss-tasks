import discord
import os
from scraper import *

intents = discord.Intents.default() 
intents.message_content = True 
intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is connected to the following server:\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')
        
@client.event
async def on_message(message):

  if message.content.startswith('\livescore'):
    try:
        live_scores = get_live_scores()
   
    except Exception as e:
        live_scores = f"Sorry!! Couldn't get the scores due to : {e}"
    await message.channel.send(live_scores)
    
  if message.content.startswith('\generate'):
    csv_generator()
    await message.channel.send("done")
    
  if message.content.startswith("\list"):
    await message.channel.send("\livescore\n\generate\n\list")
client.run(os.getenv("TOKEN"))
