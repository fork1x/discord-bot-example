import disnake
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), owner_id="537976988573368323",
                   activity=disnake.Game("/help - помощь", status=disnake.Status.online))
bot.remove_command("help")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


token = open("token.txt", "r").readline()
bot.run(token)