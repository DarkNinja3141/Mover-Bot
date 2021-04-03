from discord.abc import GuildChannel
from discord_slash import SlashContext, cog_ext, SlashCommandOptionType
from discord_slash.utils import manage_commands

from .MyCog import MyCog
from command.move import *
from util.error import CommandUseFailure


class MoveSlashCommands(MyCog):
    def __init__(self, bot):
        super().__init__(bot)

    @cog_ext.cog_slash(name="move",
                       description="Request the conversation moves to another text channel",
                       options=[
                           manage_commands.create_option(
                               name="destination",
                               description="Where to move the conversation to",
                               option_type=SlashCommandOptionType.CHANNEL,
                               required=True,
                           ),
                       ])
                       #guild_ids=[514223116893945856])
    async def move_slash(self, ctx: SlashContext, destination: GuildChannel):
        try:
            _, destination = move_check(ctx, destination)
        except CommandUseFailure as error:
            await ctx.respond(eat=True)
            await ctx.send_hidden(content=error.message)
        origin_text, dest_text = get_pre_move_text()
        await ctx.respond(eat=False)
        origin = await ctx.send(content=origin_text)
        dest = await destination.send(dest_text)
        origin_embed, dest_embed = get_move_text(origin, dest, ctx.author)
        await origin.edit(content="", embed=origin_embed)
        await dest.edit(content=None, embed=dest_embed)
