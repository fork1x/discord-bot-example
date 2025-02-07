import disnake
from disnake.ext import commands

class KickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Кикнуть участника")
    async def kick(self, inter, member: disnake.Member, reason: str = commands.Param("не указана")):
        await member.kick(reason=reason)
        await inter.response.send_message(f"Пользователь **{member}** был кикнут по причине: **{reason}**.")

def setup(bot):
    bot.add_cog(KickCommand(bot))
    print(f"{__name__} ✔")