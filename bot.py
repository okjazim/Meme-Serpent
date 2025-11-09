import discord
import time
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

def get_meme():
  response = requests.get('https://meme-api.com/gimme/memes')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
    async def on_message(self, message):
        if message.author == self.user:
            return
    
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
            
        elif message.content.startswith('$time'):
            current_time = time.strftime("%H:%M:%S", time.localtime())
            await message.channel.send(f"The current time is: {current_time}")
            
        elif message.content.startswith('$meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN) # Replace with your own token.