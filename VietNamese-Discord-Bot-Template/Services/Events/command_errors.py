import discord
from discord.ext import commands


class CommandErrors(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(
        self,
        ctx: commands.Context,
        error: commands.CommandError,
    ) -> None:
        if isinstance(error, commands.CommandNotFound):
            return

        error = getattr(error, "original", error)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Lenh dang thieu tham so bat buoc.", mention_author=False)
            return

        if isinstance(error, commands.BadArgument):
            await ctx.reply("Tham so khong hop le.", mention_author=False)
            return

        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("Ban khong co quyen dung lenh nay.", mention_author=False)
            return

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("Bot dang thieu quyen de chay lenh nay.", mention_author=False)
            return

        embed = discord.Embed(
            title="Lenh bi loi",
            description=f"```py\n{error}\n```",
            color=discord.Color.red(),
        )
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandErrors(bot))
