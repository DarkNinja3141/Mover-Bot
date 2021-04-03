from typing import Union

from discord import Message, Member, Color, Embed, TextChannel
from discord.abc import GuildChannel
from discord.ext.commands import Context
from discord_slash import SlashContext

from util.error import CommandUseFailure

__all__ = [
    "move_check",
    "get_pre_move_text",
    "get_move_text",
]


def move_check(ctx: Union[Context, SlashContext], destination: GuildChannel) -> (Union[Context, SlashContext], TextChannel):
    if ctx.guild is None:
        raise CommandUseFailure("Command must be performed in a guild.")
    if not isinstance(destination, TextChannel):
        raise CommandUseFailure("Destination must be a text channel.")
    author: Member = ctx.author
    bot: Member = ctx.guild.get_member(ctx.bot.user.id)
    origin: TextChannel = ctx.channel
    if origin == destination:
        raise CommandUseFailure("Destination must be a different channel.")
    if not destination.permissions_for(author).send_messages:
        raise CommandUseFailure("You must have permission to send messages in the destination channel.")
    if not origin.permissions_for(bot).send_messages:
        raise CommandUseFailure("Bot must have permission to send messages in the current channel.")
    if not destination.permissions_for(bot).send_messages:
        raise CommandUseFailure("Bot must have permission to send messages in the destination channel.")
    return ctx, destination  # Return passed parameters in order to perform type casting on destination


def get_pre_move_text():
    return "Dialing...", "Incoming wormhole..."


def get_move_text(origin: Message, dest: Message, author: Member):
    dest_text = f"""{author.mention} has dialed in an incoming wormhole from {origin.channel.mention}.
               [(A conversation)]({origin.jump_url}) has been requested to move here."""
    origin_text = f"""{author.mention} has dialed a wormhole to {dest.channel.mention}.
               The conversation has been requested to move there. [(Click)]({dest.jump_url})"""
    color = Color.random()
    dest_embed = Embed(color=color, title="Unscheduled Offworld Activation...", description=dest_text)
    origin_embed = Embed(color=color, title="Chevron 7 Locked...", description=origin_text)
    return origin_embed, dest_embed
