import telebot
from telebot import types
import pickle


# keys
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('tele_api')

bot = telebot.TeleBot(api)

timetable = pickle.load(open('timetable.pickle', 'rb'))
days = ['tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_timetable(day, dpt='aiml_2020_0'):
    global timetable
    per = timetable[dpt][day]
    tim = timetable[timetable[dpt]['tim'][day]]
    te = ''
    for i in range(len(per)):
        te += tim[i]+'\n'
        te += timetable[dpt]['map'][timetable[dpt][day][i]]+'\n\n'
    return te

@bot.message_handler(func=lambda m: True)
def echo(message):
    global get_timetable
    msg = message.text
    sender_id = message.chat.id
    # timetable
    if msg=='/timetable':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        itembtna = types.KeyboardButton('Tuesday')
        itembtnv = types.KeyboardButton('Wednesday')
        itembtnc = types.KeyboardButton('Thursday')
        itembtnd = types.KeyboardButton('Friday')
        itembtne = types.KeyboardButton('Saturday')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(sender_id, "Choose one day:", reply_markup=markup)

        # time talbe function
    elif msg.lower() in days:
        te = get_timetable(msg.lower()[:3])
        bot.send_message(sender_id, te)


bot.infinity_polling()