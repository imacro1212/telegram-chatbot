import os
import telebot
from utils.location import LocationList

API_TOKEN = '8033900249:AAFtZjonjtsBz_8jLyeqMNlDJAiPoCbRxsc'
bot = telebot.TeleBot(API_TOKEN)
location_list = LocationList()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Location Bot! Send me a place name and I'll give you the coordinates.")

@bot.message_handler(func=lambda message: True)
def send_coordinates(message):
    place = message.text
    coordinates = location_list.get_coordinates(place)
    if coordinates:
        latitude, longitude = coordinates
        bot.send_message(message.chat.id, f"{latitude}, {longitude}")
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't find the coordinates for that place.")

if __name__ == '__main__':
    bot.polling(none_stop=True)