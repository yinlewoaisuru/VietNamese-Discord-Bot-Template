from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands


class SlashKick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick mot thanh vien khoi server")
    @app_commands.default_permissions(kick_members=True)
    @app_commands.describe(member="Thanh vien can kick", reason="Ly do kick")
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: Optional[str] = None,
    ) -> None:
        guild = interaction.guild
        actor = interaction.user
        if guild is None or not isinstance(actor, discord.Member):
            await interaction.response.send_message(
                "Lenh nay chi dung duoc trong server.",
                ephemeral=True,
            )
            return

        bot_member = guild.me
        if bot_member is None:
            await interaction.response.send_message("Khong tim thay bot trong server.", ephemeral=True)
            return

        if member.id in (actor.id, bot_member.id):
            await interaction.response.send_message("Khong the kick doi tuong nay.", ephemeral=True)
            return

        if member.id == guild.owner_id:
            await interaction.response.send_message("Khong the kick owner server.", ephemeral=True)
            return

        if member.top_role >= bot_member.top_role:
            await interaction.response.send_message(
                "Role cua bot thap hon hoac bang thanh vien can kick.",
                ephemeral=True,
            )
            return

        if actor.id != guild.owner_id and member.top_role >= actor.top_role:
            await interaction.response.send_message(
                "Ban khong the kick thanh vien co role cao hon hoac bang ban.",
                ephemeral=True,
            )
            return

        reason = reason or "Khong co ly do"
        await interaction.response.defer(ephemeral=True)
        await member.kick(reason=f"{reason} | Boi {actor} ({actor.id})")
        await interaction.followup.send(
            f"Da kick {member.mention}. Ly do: `{reason}`",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashKick(bot))
