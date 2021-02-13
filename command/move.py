from discord import Message, Member, Color, Embed


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
