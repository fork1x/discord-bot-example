import disnake
import os
from datetime import datetime
from disnake.ext import commands

cogs_folder = "cogs"
cogs_name = os.listdir(cogs_folder)
if ("__pycache__" in cogs_name) and ("events.py" in cogs_name):
    cogs_name.remove("__pycache__")
    cogs_name.remove("events.py")


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Помощь")
    async def help(self, inter):  # ctx = inter (ctx - context)
        embed = disnake.Embed(
            title="Это помощь",
            description=f"Команды доступные в боте: {', '.join([f'`/{cog[:-3]}`' for cog in cogs_name])}.",
            colour=disnake.Colour.green(),
            timestamp=datetime.utcnow()
        )
        await inter.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.get_channel(1337376621266473030).send(f"{__name__} ✔")


def setup(bot):
    bot.add_cog(HelpCommand(bot))
    print(f"{__name__} ✔")