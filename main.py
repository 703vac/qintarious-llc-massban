import discord
from discord.ext import commands
from colorama import *
import os









client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    os.system("cls")
    print(Fore.BLUE + f'Logged in as {client.user}')
    print(Fore.BLUE + "qintarious llc massban is ready")
    print(Fore.BLUE + "\n\nCommands:")
    print(Fore.BLUE + """\n 
          [ - more commands coming soon
          $massban - bans everyone
          ]
          """)




@client.command()
async def massban(ctx):
    os.system('cls')
    for guild in client.guilds:
        for member in guild.members:
            try:
                await member.ban()
                print(f"{Fore.BLUE}banned {member.display_name}")
            except:
                pass


client.run('')
