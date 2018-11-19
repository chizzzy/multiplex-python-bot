from telegram.ext import Updater
from telegram.ext import CommandHandler
from Data import Data
from settings_local import bot_token


def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Кулити, вот доступные команды: \n" +
                    '/start - начать сначала \n' + '/show_movies - глянуть идущие в кино фильмы')


def show_movies(bot, update):
    titles = data.get_movie_titles()
    bot.sendMessage(chat_id=update.message.chat_id, text='Вот ваши фильмы, как заказывали: \n' + titles)


data = Data()
data.get_page()
data.get_movie_titles()
updater = Updater(token=bot_token)
# тут токен, который выдал вам Ботский Отец!
start_handler = CommandHandler('start', start)  # этот обработчик реагирует # только на команду /start
movies_list_handler = CommandHandler('show_movies', show_movies)
updater.dispatcher.add_handler(movies_list_handler)
updater.dispatcher.add_handler(start_handler)  # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!
