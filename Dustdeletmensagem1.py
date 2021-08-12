import discord, asyncio
import shutil
import subprocess
import psutil
import logging
from sys import argv
from os import system
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system

def logo():
    try:
        msg = f"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------
\\|       \ |  |  |  |     /       ||           |    /       | /      ||   _  \     |  | |   _  \  |           |(_ )   /_ | |____  | |____  | |____  |   //
\\|  .--.  ||  |  |  |    |   (----``---|  |----`   |   (----`|  ,----'|  |_)  |    |  | |  |_)  | `---|  |----` |/     | |     / /      / /      / /    //
\\|  |  |  ||  |  |  |     \   \        |  |         \   \    |  |     |      /     |  | |   ___/      |  |             | |    / /      / /      / /     //
\\|  '--'  ||  `--'  | .----)   |       |  |     .----)   |   |  `----.|  |\  \----.|  | |  |          |  |             | |   / /      / /      / /      //
\\|_______/  \______/  |_______/        |__|     |_______/     \______|| _| `._____||__| | _|          |__|             |_|  /_/      /_/      /_/       //
-----------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------
 """
        for l in msg:
            print(l, end="")
    except KeyboardInterrupt:

        sys.exit()
logo()



print('  ')
print('▃▃▃▃▃▃▃▃ Dust Comandos Dell ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('▍'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('▍「1」 limpar : (Digite "limpar" para Deletar mensagens mamaco)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('▍「2」 limpartudo : (Digite "limpartudo" para Deletar todas mensagens seu virgem )'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('▍'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('▍▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()
token = "ODU0MDMwMDIyNDMyMjYwMTE4.YMd_5A.lafV9kAilh6xAZz9MvuSnf3Qv6k"

def murder(cmd):
    subprocess.call(cmd, shell=True)
@client.event

async def on_ready():
    width = shutil.get_terminal_size().columns
    def ui():
        print()
        print("Developer/Dust' #1777".center(width))
        print()
        print("[-] Conectado como : {0} [-]".format(client.user).center(width))
        print()
    ui()

@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel
        if commands[0] == 'limpar':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'limpartudo':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

client.run(token, bot=False)

