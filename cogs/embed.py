import disnake
from disnake.ext import commands

class EmbedCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Создание простого эмбеда")
    async def embed(self, inter, title: str, description: str, color: int = commands.Param(
        0x00ff00, description="Цвет в HEX")):
        embed = disnake.Embed(
            title=title,
            colour=disnake.Colour(color),
            description=description
        )
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(EmbedCommand(bot))
    print(f"{__name__} ✔")