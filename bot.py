import discord
from discord.ext import commands
from discord import app_commands
import requests
import os
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='/', intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

def get_random_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} ... {joke['punchline']}"
    return "Sorry, couldn't fetch a joke right now."

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    if response.status_code == 200:
        json_data = response.json()
        return json_data.get('url', "Couldn't get a meme right now.")
    return "Couldn't get a meme right now."

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.tree.command(name="joke", description="Get a random joke")
async def joke(interaction: discord.Interaction):
    joke_text = get_random_joke()
    await interaction.response.send_message(joke_text)

@bot.tree.command(name="meme", description="Get a random meme")
async def meme(interaction: discord.Interaction):
    meme_url = get_meme()
    await interaction.response.send_message(meme_url)
    
@bot.tree.command(name="userinfo", description="Show your user info")
async def userinfo(interaction: discord.Interaction):
    user = interaction.user
    info = (
        f"User Info for {user.name}#{user.discriminator}\n"
        f"- Created At: {user.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
        f"- Bot: {user.bot}"
    )
    await interaction.response.send_message(info)

@bot.tree.command(name="coinflip", description="Flip a coin")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"The coin landed on **{result}**!")

@bot.tree.command(name="roll", description="Roll a six-sided dice")
async def roll(interaction: discord.Interaction):
    value = random.randint(1, 6)
    await interaction.response.send_message(f"You rolled a **{value}**!")

@bot.tree.command(name="random", description="Generate a random number between 1 and maximum")
async def random_number(interaction: discord.Interaction, maximum: int):
    number = random.randint(1, maximum)
    await interaction.response.send_message(f"Your random number is **{number}**!")

@bot.tree.command(name="rps", description="Play Rock-Paper-Scissors")
async def rps(interaction: discord.Interaction, move: str):
    moves = ["rock", "paper", "scissors"]
    move = move.lower()
    if move not in moves:
        await interaction.response.send_message("Choose: rock, paper, or scissors!")
        return
    bot_move = random.choice(moves)
    result = "Draw!"
    if (move == "rock" and bot_move == "scissors") or \
       (move == "paper" and bot_move == "rock") or \
       (move == "scissors" and bot_move == "paper"):
        result = "You win!"
    elif move != bot_move:
        result = "Bot wins!"
    await interaction.response.send_message(f"You chose `{move}`, bot chose `{bot_move}` — {result}")

@bot.tree.command(name="commands", description="List all available commands")
async def commands_list(interaction: discord.Interaction):
    commands_text = (
        "**Available Commands:**\n"
        "/joke - Get a random joke\n"
        "/meme - Get a random meme\n"
        "/userinfo - Show your user info\n"
        "/coinflip - Flip a coin\n"
        "/roll - Roll a six-sided dice\n"
        "/random - Generate random number\n"
        "/rps - Play Rock-Paper-Scissors\n"
        "/commands - Show this command list\n"
    )
    await interaction.response.send_message(commands_text)

bot.run(TOKEN)
