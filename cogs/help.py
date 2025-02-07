import disnake
import os
from disnake.ext import commands

cogs_folder = "cogs"
cogs_name = []
for root, dirs, files in os.walk(cogs_folder):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            cogs_name.append(file)


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