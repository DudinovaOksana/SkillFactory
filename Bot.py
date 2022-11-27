import telebot

TOKEN = "5676800651:AAGQD3wKtjjxNES0Xjn92FQMEg5WXK9rPgM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo',])
def answer_to_photo(message: telebot.types.Message):
    bot.reply_to(message, "Nice meme XDD")



# @bot.message_handler(content_types=['voice', ])
# def function_name(message: telebot.types.Message):
#     bot.send_message(message.chat.id, "Nice meme XDD")

bot.polling(none_stop=True)
