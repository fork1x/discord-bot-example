import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), owner_id="537976988573368323",
                   activity=disnake.Game("/help", status=disnake.Status.dnd, description="Описание"))
bot.remove_command("help")

bot.load_extension("cogs.help")
bot.load_extension("cogs.server_info")
bot.load_extension("cogs.events")
bot.load_extension("cogs.clear")
bot.load_extension("cogs.embed")


token = open("token.txt", "r").readline()
bot.run(token)