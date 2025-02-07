import disnake
from disnake.ext import commands


class ServerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Информация о сервере")
    async def server_info(self, inter):
        guild_created_at = inter.guild.created_at.strftime('%d.%m.%Y')
        language = inter.guild.preferred_locale

        match language:
            case 'en-US':
                language = 'English (US)'
            case 'en-GB':
                language = 'English (GB)'
            case 'uk':
                language = 'Ukrainian (UA)'
            case 'pl':
                language = 'Polish (PL)'
            case 'ru':
                language = 'Russian (RU)'
            case _:
                language = 'Другой'


        embed = disnake.Embed(
            title="Информация о сервере",
            colour=disnake.Colour.green(),
            description=(
                f"Название сервера: {inter.guild.name}\n"
                f"Количество участников: {inter.guild.member_count}\n"
                f"Создатель сервера: {inter.guild.owner}\n"
                f"Создан: {guild_created_at}\n"
                f"Предпочитаемый язык: {language}\n"
                f"ID сервера: {inter.guild.id}"
            )
        ).set_thumbnail(url=inter.guild.icon.url)

        await inter.response.send_message(embed=embed)
        print(inter.guild.preferred_locale)


def setup(bot):
    bot.add_cog(ServerCommand(bot))
    print(f"{__name__} ✔")