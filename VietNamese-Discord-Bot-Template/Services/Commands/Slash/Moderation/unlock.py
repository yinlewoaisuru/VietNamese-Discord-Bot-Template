from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands


class SlashUnlock(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="unlock", description="Mo khoa kenh chat")
    @app_commands.default_permissions(manage_channels=True)
    @app_commands.describe(channel="Kenh can mo khoa", reason="Ly do mo khoa")
    async def unlock(
        self,
        interaction: discord.Interaction,
        channel: Optional[discord.TextChannel] = None,
        reason: Optional[str] = None,
    ) -> None:
        guild = interaction.guild
        target = channel or interaction.channel
        if guild is None or not isinstance(target, discord.TextChannel):
            await interaction.response.send_message(
                "Lenh nay chi dung duoc trong text channel.",
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
        overwrite = target.overwrites_for(guild.default_role)
        overwrite.send_messages = None

        await interaction.response.defer(ephemeral=True)
        await target.set_permissions(
            guild.default_role,
            overwrite=None if overwrite.is_empty() else overwrite,
            reason=f"{reason} | Boi {interaction.user} ({interaction.user.id})",
        )
        await interaction.followup.send(
            f"Da mo khoa {target.mention}. Ly do: `{reason}`",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashUnlock(bot))
