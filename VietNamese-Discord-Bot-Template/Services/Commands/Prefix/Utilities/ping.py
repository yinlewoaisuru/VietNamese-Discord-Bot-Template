from discord.ext import commands


class PrefixPing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", aliases=["latency"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx: commands.Context) -> None:
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f"Pong! `{latency}ms`", mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PrefixPing(bot))
