import disnake
from disnake.ext import commands

class WelcomeMembers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel  # Отправка сообщения в системный канал
        if channel is not None:
            embed = disnake.Embed(
                title=f"Добро пожаловать на сервер {member.guild.name}!",
                description=f"Привет, {member.mention}! Мы рады видеть тебя на нашем сервере!",
                color=disnake.Color.green()
            )
            embed.set_footer(text=f"Мы теперь насчитываем {member.guild.member_count} участников.")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel  # Отправка сообщения в системный канал
        if channel is not None:
            embed = disnake.Embed(
                title=f"Пока, {member.name}!",
                description=f"Мы будем скучать по тебе, {member.name}.",
                color=disnake.Color.red()
            )
            embed.set_footer(text=f"Мы теперь насчитываем {member.guild.member_count} участников.")
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(WelcomeMembers(bot))
    print(f"{__name__} ✔")