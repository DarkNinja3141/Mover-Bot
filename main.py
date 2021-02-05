import random
import signal
import time

from discord import TextChannel, Message, Member, Embed, Color, Status, Intents
from discord.abc import GuildChannel
from discord.ext import commands
from discord.ext.commands import Bot, Context, ConversionError
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
from discord_slash.utils import manage_commands

from config import config, Config


class MyBot(Bot):
    def __init__(self, config_: Config):
        self.config: Config = config_
        intents = Intents.default()
        intents.members = True
        super().__init__(command_prefix=self.config.prefix, owner_id=self.config.owner,
                         status=Status.online,
                         intents=intents)
        self.loop.create_task(self.startup())
        self.remove_command("help")  # Remove help command

    async def on_command_error(self, ctx: Context, exception):
        pass

    def _signal(self):
        try:
            self.loop.remove_signal_handler(signal.SIGTERM)
            self.loop.add_signal_handler(signal.SIGTERM, lambda: self.loop.create_task(self.terminate()))
        except NotImplementedError:
            pass

    async def startup(self):
        await self.wait_until_ready()
        self._signal()
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def terminate(self):
        try:
            await self.change_presence(status=Status.offline)
        finally:
            await self.logout()
            time.sleep(1)


client: MyBot = MyBot(config)
slash = SlashCommand(client, auto_register=True, auto_delete=True)


@client.command(name="v")
@commands.guild_only()
async def move_command(ctx: Context, channel: TextChannel):
    origin = await ctx.send("Dialing...")
    dest = await channel.send("Incoming wormhole...")
    origin_embed, dest_embed = get_move_text(origin, dest, ctx.author)
    await origin.edit(content=None, embed=origin_embed)
    await dest.edit(content=None, embed=dest_embed)


@move_command.error
async def move_error(ctx: Context, error: Exception):
    if isinstance(error, ConversionError):
        pass
    else:
        raise error


@slash.slash(name="move",
             description="Request the conversation moves to another text channel",
             options=[
                 manage_commands.create_option(
                     name="destination",
                     description="Where to move the conversation to",
                     option_type=SlashCommandOptionType.CHANNEL,
                     required=True
                 )
             ])
async def move_slash(ctx: SlashContext, destination: GuildChannel):
    if not isinstance(destination, TextChannel):
        await move_slash_error(ctx, destination)
        return
    await ctx.respond(eat=False)
    origin = await ctx.send(content="Dialing...")
    dest = await destination.send("Incoming wormhole...")
    origin_embed, dest_embed = get_move_text(origin, dest, ctx.author)
    await origin.edit(content="", embed=origin_embed)
    await dest.edit(content=None, embed=dest_embed)


async def move_slash_error(ctx: SlashContext, destination: GuildChannel):
    await ctx.send_hidden(content="Destination must be a text channel.")


def get_move_text(origin: Message, dest: Message, author: Member):
    dest_text = f"""{author.mention} has dialed in an incoming wormhole from {origin.channel.mention}.
               [(A conversation)]({origin.jump_url}) has been requested to move here."""
    origin_text = f"""{author.mention} has dialed a wormhole to {dest.channel.mention}.
               The conversation has been requested to move there. [(Click)]({dest.jump_url})"""
    color = Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    dest_embed = Embed(color=color, title="Unscheduled Offworld Activation...", description=dest_text)
    origin_embed = Embed(color=color, title="Chevron 7 Locked...", description=origin_text)
    return origin_embed, dest_embed


if __name__ == "__main__":
    client.run(config.token)
