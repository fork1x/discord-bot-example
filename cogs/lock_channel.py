import disnake
from disnake.ext import commands

class LockChannelCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Закрыть канал")
    @commands.has_permissions(administrator=True)
    async def lock_channel(self, inter, channel: disnake.TextChannel = commands.Param(description="Канал для закрытия",)):
        await inter.channel.set_permissions(inter.guild.default_role, send_messages=False)
        await inter.response.send_message(f"Канал **{channel}** успешно закрыт.")

    @lock_channel.error
    async def kick_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("У вас нет прав администратора для выполнения этой команды.",
                                              ephemeral=True)

def setup(bot):
    bot.add_cog(LockChannelCommand(bot))
    print(f"{__name__} ✔")