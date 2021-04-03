# Mover, a bot for Discord

Mover is a simple bot for creating quick links to jump between channels. The intention is to help move conversations to the appropriate channels, smoothly and effortlessly.

Add it to your server using [this link](https://discord.com/api/oauth2/authorize?client_id=777717464280596550&permissions=2048&scope=bot%20applications.commands).

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
