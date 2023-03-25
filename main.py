import os
import sys
import subprocess
import socket

import discord
from discord import app_commands
from dotenv import load_dotenv


def get_bot_token():
    result = os.getenv('BOT_TOKEN')
    if result:
        return result
    print("Set your Bot Token in `settings.properties`")
    sys.exit()


def get_ip():
    try:
        ip = subprocess.check_output(['hostname', '-I']).decode('UTF-8')
    except:
        hostname = socket.gethostname()
        ip = str(socket.gethostbyname(hostname))
    return ip


def get_hostname():
    try:
        hostname = socket.gethostname()
    except:
        hostname = subprocess.check_output(['hostname']).decode('UTF-8')
    return hostname


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="ip", description="Get IP Address of the Server", guild=discord.Object(id=928336424514752534))
async def ip_command(interaction):
    ip = get_ip()
    _embed = discord.Embed(
        title="`" + ip + "`",
        description="sent from `" + get_hostname() + "`",
        color=0x1e1e1e,
    )
    _embed.set_author(name="open in browser", url="http://" + ip)
    _embed.set_footer(
        text="@showw v2",
    )
    await interaction.response.send_message(embed=_embed)

@client.event
async def on_ready():
    print(client.guilds)
    for guild in client.guilds:
        await tree.sync(guild=guild)
    print(f'We have logged in as {client.user}')

if __name__ == '__main__':
    load_dotenv()
    client.run(get_bot_token())
