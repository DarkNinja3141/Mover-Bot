import random

from discord import TextChannel, Message, Member, Embed, Color
from discord.ext import commands
from discord.ext.commands import Bot, Context, ConversionError

from config import config, Config


class MyBot(Bot):
    def __init__(self, config_: Config):
        self.config: Config = config_
        super().__init__(command_prefix=self.config.prefix, owner_id=self.config.owner,
                         chunk_guilds_at_startup=False)
        self.loop.create_task(self.startup())

    async def startup(self):
        await self.wait_until_ready()
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


client: MyBot = MyBot(config)


@client.command(name="logout")
async def logout(ctx: Context):
    await client.logout()


@client.command(name="v")
@commands.guild_only()
async def move_command(ctx: Context, channel: TextChannel):
    origin = await ctx.send("Dialing...")
    dest = await channel.send("Incoming wormhole...")
    await move(origin, dest, ctx.author)


@move_command.error
async def move_error(ctx: Context, error: Exception):
    if isinstance(error, ConversionError):
        pass
    else:
        raise error


async def move(origin: Message, dest: Message, author: Member):
    dest_text = f"""{author.mention} has dialed in an incoming wormhole from {origin.channel.mention}.
               [(A conversation)]({origin.jump_url}) has been requested to move here."""
    origin_text = f"""{author.mention} has dialed a wormhole to {dest.channel.mention}.
               The conversation has been requested to move there. [(Click)]({dest.jump_url})"""
    color = Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    dest_embed = Embed(color=color, title="Unscheduled Offworld Activation...", description=dest_text)
    origin_embed = Embed(color=color, title="Chevron 7 Locked...", description=origin_text)
    await dest.edit(content=None, embed=dest_embed)
    await origin.edit(content=None, embed=origin_embed)


if __name__ == "__main__":
    client.run(config.token)
