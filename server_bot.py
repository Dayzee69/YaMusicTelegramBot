import json
import os
import telebot
from telebot import types
import logging
import threading
import time

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s',
  filename='/home/dayzee/YaMusicTelegramBot/log/bot.log',
  filemode='a'
)
logger = logging.getLogger()

logger.info('Бот запущен')

with open('settings.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

bot = telebot.TeleBot(config['bot_token'])

def run_polling():
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Polling error: {e}")
        time.sleep(15)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f'Привет, {message.chat.first_name}!&#10&#10Я бот для добавления треков в очередь Яндекс.Музыка.&#10Напиши мне в чат команду "Гайд" и я расскажу, как я работаю', parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    gaid = '''Главная моя функция - это добавлять треки в текущую очередь. Для этого мне нужна ссылка на трек. Получить ее можно двумя способами.&#10&#10Первый способ. Я умею искать треки, если известно точное наименование исполнителя и название трека, то можно прислать мне сообщение "@brooklite_yamusic_bot Найди {Исполнитель}-{Название трека}".&#10&#10Пример:&#10&#10@brooklite_yamusic_bot Найди Michael Jackson-Billie Jean Обязательно с разделителем "-" без пробелов, чтобы я понял, где Исполнитель, а где Название трека. Если изветсно только название исполнителя или только название трека, то можно написать "@brooklite_spotify_bot Найди {что искать}"&#10&#10Пример:&#10&#10@brooklite_spotify_bot Найди ABBA&#10&#10В ответ на такое сообщение пришлю варианты поиска в виде двух кнопок: "Искать по исполнителю" и "Искать по названию трека". После нажатия на кнопку - вывожу роезультат. В чате появятся 10 треков, которые мне удалось найти. Под каждым вариантом будет кнопка "Добавить в очередь", которая добавит трек в очередь. Через 5 минут история поиска будет удалена, чтобы не засорять чат.&#10&#10Переходим ко второму варианту. Если по результату поиска не удалось найти, что хотелось, то можно поискать непосредственно в поиске Spotify. В меню кнопка "Spotify" откроет поиск в приложении или в браузере, если приложение не установлено.&#10&#10В Яндекс.Музыка на выбранном треке нужно нажать ... -> "Поделиться" -> "Больше" -> Telegram -> и прислать мне, боту BrookLite. Либо нажать ... ->  "Поделиться" -> "Скопировать ссылку" -> и прислать ссылку мне в этот чат. Я добавлю твой трек в очередь. &#10&#10Еще я могу показать текущую очередь и что сейчас играет. в меню кнопка "Показать очередь"'''
    bot.send_message(message.chat.id, gaid, parse_mode='html')

if __name__ == '__main__':
    polling_thread = threading.Thread(target=run_polling)
    polling_thread.start()
    polling_thread.join()