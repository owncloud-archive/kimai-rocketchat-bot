from rocketchat import RocketChatBot, RocketChatClient

bot = RocketChatBot('pybot','12345',server='localhost:3000',ssl=False)

def bookingHandler(bot, message):

  mentions = ""
  for name in message['mentions']:
    mentions += name['username'] + " "

  bot.sendMessage(message['rid'], "yo @" + message['u']['username'] + ", booked for " + mentions)


bot.addPrefixHandler('book', bookingHandler)

bot.start()
