from disnake.ext import commands


class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Очистка сообщений")
    async def clear(self, inter, amount: int = commands.Param(1, description="Количество сообщений")):
        await inter.channel.purge(limit=amount)
        if amount == 1:
            await inter.response.send_message(f"Удалено {amount} сообщение.")
        elif amount == 2 or amount == 3 or amount == 4:
            await inter.response.send_message(f"Удалено {amount} сообщения.")
        else:
            await inter.response.send_message(f"Удалено {amount} сообщений.")

def setup(bot):
    bot.add_cog(ClearCommand(bot))
    print(f"{__name__} ✔")