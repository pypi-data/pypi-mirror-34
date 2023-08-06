# Gamest Discord Notification Service

This plugin enables [gamest](https://github.com/sopoforic/gamest) to send
notifications to a discord webhook.

## Installation

Install with pip:

```
pip install gamest-discord-notification-service
```

## Configuration

The configuration is located in
`%LOCALAPPDATA%\gamest\DiscordNotificationService.conf`. The default
configuration is:

```
[DiscordNotificationService]
# Set the URL of the webhook you wish to notify below. To notify multiple
# webhooks, put one webhook per line, indenting each line after the first.
#
# webhook_url = https://discordapp.com/api/webhooks/...
#     https://discordapp.com/api/webhooks/...
#     https://discordapp.com/api/webhooks/...

# You should probably set this to your discord nickname, but it can be set to
# anything. If you also set discord_id then whenever a notification @mentions
# you, it will use your discord nickname instead of what you set here.
#
# user_name = Gamest User

# You can get your discord ID by enabling Developer Mode in discord's settings,
# then right-clicking your name in the user list and clicking 'Copy ID'. If you
# set this, then any notifications sent to discord that include your username
# will @mention you.
#
# discord_id = xxx
```

## License

Copyright (C) 2018  Tracy Poff

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
