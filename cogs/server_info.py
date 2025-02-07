import datetime

import disnake
from disnake.ext import commands


class ServerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Информация о сервере")
    async def server_info(self, inter):
        embed = disnake.Embed(
            title="Информация о сервере",
            timestamp=datetime.datetime.utcnow(),
            colour=disnake.Colour.green(),
            description=f"Название сервера: {inter.guild.name}\nКоличество участников: {inter.guild.member_count}"
        )
        await inter.response.send_message(embed=embed)



def setup(bot):
    bot.add_cog(ServerCommand(bot))
    print(f"{__name__} ✔")

