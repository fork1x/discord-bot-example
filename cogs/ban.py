import disnake
from disnake.ext import commands

class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Забанить участника")
    @commands.has_permissions(administrator=True)
    async def ban(self, inter, member: disnake.Member, reason: str = commands.Param("не указана")):
        if member.top_role >= inter.author.top_role:
            return await inter.response.send_message("Вы не можете забанить данного участника.")
        await member.send(f"Вы были забанены на сервере {inter.guild.name} по причине: **{reason}**.")
        await member.ban(reason=reason)
        await inter.response.send_message(f"Пользователь **{member}** был забанен по причине: **{reason}**.")

    @ban.error
    async def kick_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("У вас нет прав администратора для выполнения этой команды.",
                                              ephemeral=True)

def setup(bot):
    bot.add_cog(BanCommand(bot))
    print(f"{__name__} ✔")