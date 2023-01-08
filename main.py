import discord

import DiscordHandler.DiscordHandler as dh
import Service.ServiceRunner as sr

if __name__ == '__main__':
    bot = dh.DiscordHandler(intents=discord.Intents.default())
    bot.run(sr.get_bot_token())
