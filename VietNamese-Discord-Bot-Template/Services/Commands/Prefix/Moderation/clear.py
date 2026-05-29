from discord.ext import commands


class PrefixClear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="clear", aliases=["purge"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clear(
        self,
        ctx: commands.Context,
        amount: int,
        *,
        reason: str = "Khong co ly do",
    ) -> None:
        if amount < 1 or amount > 100:
            await ctx.reply("So luong tin nhan phai tu 1 den 100.", mention_author=False)
            return

        deleted = await ctx.channel.purge(
            limit=amount + 1,
            reason=f"{reason} | Boi {ctx.author} ({ctx.author.id})",
        )
        count = max(len(deleted) - 1, 0)
        await ctx.send(f"Da xoa {count} tin nhan.", delete_after=5)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PrefixClear(bot))
