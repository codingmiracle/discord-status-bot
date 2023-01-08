import discord
from discord import user
import Service.ServiceRunner as sr
from DiscordHandler import messages


class DiscordHandler(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)

    async def on_ready(self):
        print("logged in at " + sr.get_ip())
        self.Call = self.user.name

    async def on_message(self, message):
        if message.author == user:
            return

        if message.content.startswith("/"):
            prompt = message.content[1:]
            if prompt.startswith("help"):
                await message.channel.send(embed=messages.help_embed)
            elif prompt.startswith("settings"):
                await message.channel.send(embed=messages.settings_embed)
            elif prompt.startswith("ip"):
                ip = sr.get_ip()
                _embed = discord.Embed(
                title="The IP Address of `" + sr.get_hostname() + "` is:",
                description="`" + ip + "`",
                color=0x1e1e1e,
                )
                _embed.set_author(name="take me to " + ip, url="http://" + ip)
                _embed.set_footer(
                    text="your ip - " + str(message.author),
                )
                await message.channel.send(embed=_embed)
            else:
                await message.channel.send(embed=messages.general_embed)
