from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="userinfo", description="Xem thong tin nguoi dung")
    @app_commands.describe(user="Nguoi dung can xem thong tin")
    async def userinfo(
        self,
        interaction: discord.Interaction,
        user: Optional[discord.Member] = None,
    ) -> None:
        if interaction.guild is None:
            await interaction.response.send_message(
                "Lenh nay chi dung duoc trong server.",
                ephemeral=True,
            )
            return

        target = user or interaction.user
        if not isinstance(target, discord.Member):
            await interaction.response.send_message(
                "Khong doc duoc thong tin thanh vien.",
                ephemeral=True,
            )
            return

        created_at = int(target.created_at.timestamp())
        joined_at = int(target.joined_at.timestamp()) if target.joined_at else None

        embed = discord.Embed(title=f"Thong tin {target}", color=discord.Color.blurple())
        embed.set_thumbnail(url=target.display_avatar.url)
        embed.add_field(name="ID", value=str(target.id), inline=True)
        embed.add_field(name="Bot", value="Co" if target.bot else "Khong", inline=True)
        embed.add_field(name="Tao tai khoan", value=f"<t:{created_at}:F>", inline=False)
        embed.add_field(
            name="Vao server",
            value=f"<t:{joined_at}:F>" if joined_at else "Khong co du lieu",
            inline=False,
        )
        embed.add_field(name="Role cao nhat", value=target.top_role.mention, inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserInfo(bot))
