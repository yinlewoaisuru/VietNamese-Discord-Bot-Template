import discord
from discord.ext import commands


class GhostPing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message) -> None:
        if message.guild is None or message.author.bot or not message.mentions:
            return

        content = message.content or "Khong doc duoc noi dung tin nhan."
        if len(content) > 1000:
            content = content[:997] + "..."

        mentions = ", ".join(user.mention for user in message.mentions[:10])
        embed = discord.Embed(
            title="Phat hien ghost ping",
            description=(
                f"Tac gia: {message.author.mention}\n"
                f"Da mention: {mentions}\n\n"
                f"```txt\n{content}\n```"
            ),
            color=discord.Color.orange(),
        )
        embed.set_footer(text=f"Channel: #{message.channel}")
        await message.channel.send(
            embed=embed,
            allowed_mentions=discord.AllowedMentions.none(),
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GhostPing(bot))
