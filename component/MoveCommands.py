from discord import TextChannel
from discord.ext import commands
from discord.ext.commands import Context, UserInputError, CommandInvokeError

from .MyCog import MyCog
from command.move import *
from util.error import CommandUseFailure


class MoveCommands(MyCog):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name="v")
    @commands.guild_only()
    async def move_command(self, ctx: Context, destination: TextChannel):
        try:
            _, destination = move_check(ctx, destination)
        except CommandUseFailure as error:
            raise error
        origin_text, dest_text = get_pre_move_text()
        origin = await ctx.send(origin_text)
        dest = await destination.send(dest_text)
        origin_embed, dest_embed = get_move_text(origin, dest, ctx.author)
        await origin.edit(content=None, embed=origin_embed)
        await dest.edit(content=None, embed=dest_embed)

    @move_command.error
    async def move_error(self, ctx: Context, error: Exception):
        if isinstance(error, UserInputError):
            pass
        elif isinstance(error, CommandInvokeError) and isinstance(error.original, CommandUseFailure):
            pass
        else:
            raise error
