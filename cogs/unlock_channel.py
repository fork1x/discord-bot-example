import disnake
from disnake.ext import commands

class UnlockChannelCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description = "Открыть канал")
    @commands.has_permissions(administrator=True)
    async def unlock_channel(self, inter, channel: disnake.TextChannel = commands.Param(description="Канал для открытия",)):
        await inter.channel.set_permissions(inter.guild.default_role, send_messages=True)
        await inter.response.send_message(f"Канал **{channel}** успешно открыт.")

    @unlock_channel.error
    async def kick_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("У вас нет прав администратора для выполнения этой команды.",
                                              ephemeral=True)

def setup(bot):
    bot.add_cog(UnlockChannelCommand(bot))
    print(f"{__name__} ✔")