import discord
from discord.ext import commands


class PrefixHelp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help", aliases=["commands"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def help(self, ctx: commands.Context) -> None:
        prefix = getattr(ctx.clean_prefix, "strip", lambda: ctx.clean_prefix)()
        embed = discord.Embed(
            title="Danh sach lenh prefix",
            description=f"Prefix hien tai: `{prefix}`",
            color=discord.Color.blurple(),
        )
        embed.add_field(name="Utilities", value="`ping`, `help`", inline=False)
        embed.add_field(name="Moderation", value="`clear`", inline=False)
        embed.add_field(name="Owner", value="`syncslash`", inline=False)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PrefixHelp(bot))
