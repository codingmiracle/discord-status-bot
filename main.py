import discord
from discord.utils import *
import socket
import subprocess

help_embed = discord.Embed(
    title="Commands",
    description="Here are all available commands:",
    color=0x1e1e1e
)
help_embed.add_field(name="`-ip` | `showip`:",
                     value="sends you the ip address of your device"
)
help_embed.add_field(name="`-settings`:",
                     value="display your current settings"
)
help_embed.add_field(name="`-name <nickname>`:",
                     value="change callphrase to nickname or false to call the bot with his name"
)
help_embed.add_field(name="`-autonf <state>`:",
                     value="enable/disable autonotify with true/false as state"
)

general_embed = discord.Embed(
    title="Invalid command",
    description="use `-help` to see all commands!"
)

settings_embed = discord.Embed(
    title="Settings",
    description="To change the settings use the commands shown in `-help`",
    color=0x1e1e1e
)

short_embed = discord.Embed(
    title="new Name set!",
    description="use the new name for calling the bot to see all commands!",
    color=0x1e1e1e
)

autonotify_embed = discord.Embed(
    title="Autonotify set!",
    description="Autonotify has been set to this channel!",
    color=0x1e1e1e
)


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


class DiscordHandler(discord.Client):
    def init(self):
        self.creator = "codingmiracle#4634"
        self.short = False
        self.usecall = True
        self.Call = "showw3"
        self.autonotify_channel = ""

    async def on_ready(self):
        print("logged in at " + get_ip())
        self.Call = self.user.name


    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(self.Call):
            msg = message.content[(len(self.Call) + 1):]
            if msg == "-help":
                help_embed.set_footer(
                    text="commandlist - " + str(self.user.name)
                )
                await message.channel.send(embed=help_embed)
            elif msg == "-ip":
                ip = get_ip()
                ip_embed = discord.Embed(
                    title="Your `" + get_hostname() + "` ip address is:",
                    description="`" + ip + "`",
                    color=0x1e1e1e,
                )
                ip_embed.set_author(name="take me to " + ip, url="http://" + ip)
                ip_embed.set_footer(
                    text="yourip - " + str(self.user.name),
                )
                await message.channel.send(embed=ip_embed)
            elif msg == "-settings":
                settings_embed = discord.Embed(
                    title="Settings",
                    description="To change the settings use the commands shown in `-help`",
                    color=0x1e1e1e
                )
                settings_embed.add_field(
                    name="wakeup call:",
                    value=self.Call
                )
                try:
                    settings_embed.add_field(
                        name="autonotify Channel:",
                        value=str(self.autonotify_channel.id)
                    )
                except:
                    settings_embed.add_field(
                        name="autonotify Channel:",
                        value="not set! use `-autonotify` to set it to a channel"
                    )
                await message.channel.send(embed=settings_embed)

            elif msg.startswith("-name"):
                self.Call = msg[len("-name") + 1:]
                await message.channel.send(embed=short_embed)

            elif msg.startswith("-autonf"):
                self.autonotify_channel = message.channel
                await message.channel.send(embed=autonotify_embed)
            else:
                general_embed.set_footer(text="invalidcommand - " + str(self.user.name))
                try:
                    await message.delete()
                    await message.channel.send(embed=general_embed, delete_after=60)
                except:
                    await message.channel.send(embed=general_embed, delete_after=60)

        elif message.content == "showip":
            ip = get_ip()
            ip_embed = discord.Embed(
                title="Your `" + get_hostname() + "` ip address is:",
                description="`" + ip + "`",
                color=0x1e1e1e,
            )
            ip_embed.set_author(name="take me to " + ip, url="http://" + ip)
            ip_embed.set_footer(
                text="yourip - " + str(self.user.name),
            )
            await message.channel.send(embed=ip_embed)



if __name__ == '__main__':
    bot = DiscordHandler()
    bot.init()
    with open('resources/bot-token.txt', 'r') as f:
        bot_token = f.readline()
        f.close()
    bot.run(bot_token)
