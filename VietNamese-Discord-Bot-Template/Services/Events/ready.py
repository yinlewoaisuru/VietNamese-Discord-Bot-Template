from discord.ext import commands


class ReadyEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._printed = False

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        if self._printed:
            return

        self._printed = True
        print(f"Bot da san sang: {self.bot.user} | Server: {len(self.bot.guilds)}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReadyEvent(bot))
