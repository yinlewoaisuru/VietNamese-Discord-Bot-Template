from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands


class SlashLockdown(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="lockdown", description="Khoa tat ca text channel")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(reason="Ly do lockdown")
    async def lockdown(
        self,
        interaction: discord.Interaction,
        reason: Optional[str] = None,
    ) -> None:
        guild = interaction.guild
        if guild is None:
            await interaction.response.send_message(
                "Lenh nay chi dung duoc trong server.",
                ephemeral=True,
            )
            return

        bot_member = guild.me
        if bot_member is None or not bot_member.guild_permissions.manage_channels:
            await interaction.response.send_message(
                "Bot thieu quyen Manage Channels.",
                ephemeral=True,
            )
            return

        reason = reason or "Khong co ly do"
        await interaction.response.defer(ephemeral=True)

        locked = 0
        failed = 0
        for channel in guild.text_channels:
            overwrite = channel.overwrites_for(guild.default_role)
            overwrite.send_messages = False
            try:
                await channel.set_permissions(
                    guild.default_role,
                    overwrite=overwrite,
                    reason=f"{reason} | Boi {interaction.user} ({interaction.user.id})",
                )
            except discord.HTTPException:
                failed += 1
            else:
                locked += 1

        await interaction.followup.send(
            f"Da lockdown {locked} kenh. That bai: {failed}. Ly do: `{reason}`",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashLockdown(bot))
