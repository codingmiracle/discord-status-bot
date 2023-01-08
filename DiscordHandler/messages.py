import discord

help_embed = discord.Embed(
    title="Help",
    description="Here are all available commands:",
    color=0x1e1e1e
)
help_embed.add_field(name="`/ip` | `showip`:",
                     value="sends you the ip address of your device"
)
help_embed.add_field(name="`/settings`:",
                     value="display your current settings"
)
help_embed.add_field(name="`/status`:",
                     value="display cpu, ram, memory and other properties of your server"
)
help_embed.add_field(name="`/autonf`:",
                     value="enable autonotify"
)

general_embed = discord.Embed(
    title="Invalid command",
    description="use `/help` to see all commands!"
)

settings_embed = discord.Embed(
    title="Settings",
    description="To change the settings use the commands shown in `/help`",
    color=0x1e1e1e
)

autonotify_embed = discord.Embed(
    title="Autonotify set!",
    description="Autonotify has been set to this channel!",
    color=0x1e1e1e
)