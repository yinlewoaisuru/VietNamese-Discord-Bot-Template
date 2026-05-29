import discord
from discord.ext import commands
import json
import os
from typing import Literal, Optional


config_path = './Setting/Config.json'
services_path = './Services'

with open(config_path, encoding='utf-8') as config_file:
    data = json.load(config_file)
    Token = data['TOKEN'].strip()
    Prefix = data['PREFIX'].strip()
    OwnerId = int(data.get('OWNER_ID', 0)) or None
    ClientId = int(data.get('CLIENT_ID', 0)) or None


if (
    not Token
    or 'TOKEN BOT' in Token.upper()
    or 'TOKEN_BOT' in Token.upper()
    or 'CUA_BAN' in Token.upper()
    or 'CỦA BẠN' in Token.upper()
    or Token.lower().startswith('bot ')
):
    raise SystemExit('Vui long dien token bot that trong Setting/Config.json. main.py khong doc token tu Setting/Env/.env.')


intents = discord.Intents.all()
intents.message_content = True


bot = commands.Bot(
    command_prefix=Prefix,
    intents=intents,
    owner_id=OwnerId,
    application_id=ClientId,
    help_command=None,
    strip_after_prefix=True
)


def get_cogs_list():
    cogs_list = []

    for root, _, files in os.walk(services_path):
        for file in files:
            if not file.endswith('.py') or file.startswith('_'):
                continue

            cogs = os.path.join(root, file)
            cogs = os.path.splitext(cogs)[0]
            cogs = cogs.replace('\\', '.').replace('/', '.')
            cogs = cogs.lstrip('.')
            cogs_list.append(cogs)

    return sorted(cogs_list)


cogs_list = get_cogs_list()


async def load_cogs():
    for cogs in cogs_list:
        try:
            await bot.load_extension(cogs)
            print(f'Load cogs {cogs} thành công')
        except commands.ExtensionAlreadyLoaded:
            pass
        except Exception as error_on_load_cogs:
            print(f'Gặp lỗi khi load cogs {cogs} ^^^{error_on_load_cogs}')


@bot.event
async def on_ready():
    print(f'Online vào bot {bot.user}')
    await load_cogs()

@bot.command()
@commands.is_owner()
async def syncslash(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


bot.run(Token)
