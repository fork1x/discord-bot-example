import disnake
from disnake.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Проверить пинг")
    async def ping(self, inter):
        await inter.response.send_message(f":ping_pong: Понг! Мой пинг: {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(PingCommand(bot))
    print(f"{__name__} ✔")