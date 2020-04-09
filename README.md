# Rocket.Chat Python Bot for time booking with Kimai

Based on a Python Connector SDK for RocketChat Realtime API.
Thanks to https://github.com/diegodorgam/python-rocketchat-bot


## Development Setup for the bot 

Tested with python3.
- `pip3 install python-meteor`
- `python3 run.py`


## Rocket.Chat Setup

Start a Rocket.Chat, if you don't have one already...
- `docker-compose up -d`

This will create a folder `data` for volume data, which you can delete after
- `docker-compose down`

If anything needs debugging, open logs
- `docker-compose logs -f`

Create user with Role Bot, and update the login in `run.py`
- username and password 
- your rocket.chat url:port


## Usage

In any project channel say: `book 2h @felix @markus`

The bot books via Kimai API 
- 2h 
- for the project, which is called exactly as the channel
- for all mentioned people, which need to have same Rocket.Chat display name 'name' as users have in Kimai

If you say in any channel `book 2h @felix #ownCloud`
the mentioned channel(s) are used for project(s) instead of the channel you posted the message in.

## Rocket.Chat SDK

### Receive messages

Register for messages `bot.addPrefixHandler('book', bookingHandler)`
Calls function `bookingHandler(bot, message)` when a message starts with "book" in any channel.

Available infos in the message for e.g "book 2h @felix #test" sent in channel General
```
{ '_id': 'Fha8KYoBvtFjmKg9P',
  '_updatedAt': datetime.datetime(2020, 4, 9, 12, 44, 33, 135000, tzinfo=datetime.timezone.utc),
  'channels': [ { '_id': 'Eso7XADufNbkq26n7', 
                  'name': 'test'}],
  'mentions': [ { '_id': 'ND4wEbMZAAFYL5Cuu',
                  'name': 'Felix Böhm',
                  'username': 'felix'}],
  'msg': 'book 2h @felix #test',
  'rid': 'GENERAL',
  'ts': datetime.datetime(2020, 4, 9, 12, 44, 33, 24000, tzinfo=datetime.timezone.utc),
  'u': { '_id': 'nwg5mPwuGCJEpwACr', 
         'name': 'Admin', 
         'username': 'admin'}
}
```

- message['msg']
- message['rid']
- message['u']['name']


### Send a message

The bot can send messages to any channel.
If you want to return in the same channel, use `message['rid']`

`bot.sendMessage(message['rid'], "Bot says hello")`


