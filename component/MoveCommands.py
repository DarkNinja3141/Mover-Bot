from discord import TextChannel
from discord.ext import commands
from discord.ext.commands import Context, ConversionError

from .MyCog import MyCog
from command.move import get_pre_move_text, get_move_text


class MoveCommands(MyCog):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name="v")
    @commands.guild_only()
    async def move_command(self, ctx: Context, channel: TextChannel):
        origin_text, dest_text = get_pre_move_text()
        origin = await ctx.send(origin_text)
        dest = await channel.send(dest_text)
        origin_embed, dest_embed = get_move_text(origin, dest, ctx.author)
        await origin.edit(content=None, embed=origin_embed)
        await dest.edit(content=None, embed=dest_embed)

    @move_command.error
    async def move_error(self, ctx: Context, error: Exception):
        if isinstance(error, ConversionError):
            pass
        else:
            raise error
