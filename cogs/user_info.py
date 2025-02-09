import disnake
from disnake.ext import commands

class UserinfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Получить информацию о пользователе")
    async def user_info(self, inter, member: disnake.Member = commands.Param(description="Укажите пользователя",
                                                                             default = None)):
        member = member or inter.author


        if member.activity:
            activity = member.activity.name


        embed = disnake.Embed(title = f"Информация о пользователе {member}", color = disnake.Color.green())
        embed.add_field(name = "Никнейм", value = member.display_name)
        embed.add_field(name = "ID", value = member.id)
        embed.add_field(name = "Аккаунт создан", value = member.created_at.strftime("%d.%m.%Y"))
        embed.add_field(name = "Присоединился к серверу", value = member.joined_at.strftime("%d.%m.%Y %H:%M:%S"))
        embed.add_field(name = "Роли", value = ", ".join([role.mention for role in member.roles]))
        if member.avatar:
            embed.set_thumbnail(url = member.avatar.url)
        await inter.response.send_message(embed = embed)

def setup(bot):
    bot.add_cog(UserinfoCommand(bot))
    print(f"{__name__} ✔")