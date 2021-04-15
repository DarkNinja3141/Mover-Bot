# Mover, a bot for Discord

[![Python version](https://img.shields.io/badge/dynamic/yaml?color=brightgreen&label=python&query=%24.python&url=https%3A%2F%2Fraw.githubusercontent.com%2FDarkNinja3141%2FMover-Bot%2Fmaster%2Fversions.yaml)](https://www.python.org/downloads/release/python-387/) [![discord.py PyPI](https://img.shields.io/badge/dynamic/yaml?color=blue&label=discord.py&query=%24%5B%22discord.py%22%5D&url=https%3A%2F%2Fraw.githubusercontent.com%2FDarkNinja3141%2FMover-Bot%2Fmaster%2Fversions.yaml)](https://pypi.org/project/discord.py/) [![discord-py-slash-command PyPI](https://img.shields.io/badge/dynamic/yaml?color=blue&label=discord-py-slash-command&query=%24%5B%22discord-py-slash-command%22%5D&url=https%3A%2F%2Fraw.githubusercontent.com%2FDarkNinja3141%2FMover-Bot%2Fmaster%2Fversions.yaml)](https://pypi.org/project/discord-py-slash-command/)

[![Discord invite](https://img.shields.io/discord/831679611150270474.svg?color=7289DA&label=Dark%27s%20Bots&logo=discord&labelColor=697EC4&logoColor=white)](https://discord.gg/SazhZEFZu5)

Mover is a simple bot for creating quick links to jump between channels. The intention is to help move conversations to the appropriate channels, smoothly and effortlessly.

Add it to your server using [this link](https://discord.com/api/oauth2/authorize?client_id=777717464280596550&permissions=18432&scope=bot%20applications.commands).

## Usage

Mover has only one command, "move". This can be invoked using an old-fashioned channel message or by using Discord's new slash commands.

The required parameter is the destination, the text channel where you want the conversation to be moved to. It must be a text channel, and the user running the command must have permission to send messages there.

When the command is run, an embed message is sent in the origin channel (where the command was run) and in the destination channel, with hyperlinks in them that link to each other.

### Slash command

`/move <destination>`

A list of channels will be shown by your discord client, however only text channels are permitted.

### Text command

`m.v <destination>`

Destination can be:
- Channel name (ex. "channel-name")
- Channel mention (ex. "#channel-mention")
- Channel ID (ex. "514223682164621323").

## License

```
Copyright © 2021 <DarkNinja3141@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
```
