import disnake
import os
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
    async def help(self, inter):
        embed = disnake.Embed(
            title="Это помощь",
            description=f"Команды доступные в боте: {', '.join([f'`/{cog[:-3]}`' for cog in cogs_name])}.",
            colour=disnake.Colour.green(),
            timestamp=disnake.utils.utcnow()
        )
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
    print(f"{__name__} ✔")