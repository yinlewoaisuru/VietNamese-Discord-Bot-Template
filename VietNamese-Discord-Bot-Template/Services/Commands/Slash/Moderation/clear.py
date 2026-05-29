from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands


class SlashClear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Xoa nhieu tin nhan trong kenh")
    @app_commands.default_permissions(manage_messages=True)
    @app_commands.describe(amount="So tin nhan can xoa", reason="Ly do xoa")
    async def clear(
        self,
        interaction: discord.Interaction,
        amount: app_commands.Range[int, 1, 100],
        reason: Optional[str] = None,
    ) -> None:
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel):
            await interaction.response.send_message(
                "Lenh nay chi dung duoc trong text channel.",
                ephemeral=True,
            )
            return

        reason = reason or "Khong co ly do"
        await interaction.response.defer(ephemeral=True)
        deleted = await channel.purge(
            limit=amount,
            reason=f"{reason} | Boi {interaction.user} ({interaction.user.id})",
        )
        await interaction.followup.send(
            f"Da xoa {len(deleted)} tin nhan. Ly do: `{reason}`",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashClear(bot))
