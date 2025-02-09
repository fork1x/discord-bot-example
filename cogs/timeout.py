import disnake
from disnake.ext import commands
import time
from datetime import timedelta

class TimeoutCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Замутить участника")
    @commands.has_permissions(administrator=True)
    async def timeout(self, inter, member: disnake.Member, duration: int, reason: str = commands.Param("не указана")):
        if member.top_role >= inter.author.top_role:
            return await inter.response.send_message("Вы не можете замутить данного участника.", ephemeral=True)
        if duration <= 0:
            return await inter.response.send_message("Время мута должно быть больше 0.", ephemeral=True)
        if duration > 10080:
            return await inter.response.send_message("Время мута не должно превышать 7 дней.", ephemeral=True)

        days, remainder = divmod(duration, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        await member.send(f"Вы были замучены на сервере {inter.guild.name} на {days} дн. {hours} ч. {minutes} мин. {seconds} сек. по причине: **{reason}**.")


        try:
            await member.timeout(duration=duration, reason=reason)
            await inter.channel.send(f"Пользователь **{member}** был замучен на {days} дн. {hours} ч. {minutes} мин."
                                     f" {seconds} сек. по причине: **{reason}**.")
        except disnake.Forbidden:
            await inter.response.send_message("У меня нет прав на это действие.", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f"Произошла ошибка:\n\n ```{e}```", ephemeral=True)

def setup(bot):
    bot.add_cog(TimeoutCommand(bot))
    print(f"{__name__} ✔")