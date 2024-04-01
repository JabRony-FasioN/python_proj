import telebot, time
from test import get_source_html
from input import load_data


with open("token.txt", 'r') as file:
    token = file.read()

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text.isdigit():
        sku = str(message.text)
        goal = get_source_html(sku)
        for i in goal:
            end_message = ' '.join(i)
            if '( ***** )' in end_message:
                pass
            else:
                bot.send_message(message.chat.id,end_message)
    elif "xlsx" in message.text:
        sku_list = load_data(message.text)
        for sku in sku_list:
      #      sku = str(sku)
            goal = get_source_html(str(sku))
            for i in goal:
                end_message = ' '.join(i)
                if '( ***** )' in end_message:
                    pass
                else:
                    time.sleep(1)

                    bot.send_message(message.chat.id,end_message)
        
    else:
        bot.send_message(message.from_user.id, "не вверный ввод данных")


bot.polling()



