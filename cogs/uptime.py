from disnake.ext import commands
import time
from datetime import timedelta

class UptimeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()  # Время запуска бота

    @commands.slash_command(description="Время работы бота")
    async def uptime(self, inter):
        uptime_seconds = time.time() - self.start_time  # Вычисляем время работы бота
        uptime_duration = timedelta(seconds=uptime_seconds)  # В формат dd:hh:mm:ss
        hours, remainder = divmod(uptime_duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        await inter.response.send_message(
            f"Время работы бота: {uptime_duration.days} дн. {hours} ч. {minutes} мин. {seconds} сек.")

def setup(bot):
    bot.add_cog(UptimeCommand(bot))
    print(f"{__name__} ✔")
