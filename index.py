from telegram.ext import CommandHandler, Updater
from Data import Data
from settings_local import bot_token


commands = ['/start - начать сначала', '/show_movies - посмотреть идущие в кино фильмы', '/book - заказать билет']


def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Ку, вот доступные команды: \n" + print_commands(commands))


def book_ticket(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Чтобы заказать билет перейдите по ссылке: https://multiplex.ua/cinema/kherson/fabrika')


def print_commands(command_list):
    return '\n'.join(command_list)


def show_movies(bot, update):
    titles = data.get_movie_titles()
    bot.sendMessage(chat_id=update.message.chat_id, text='Вот ваши фильмы, как заказывали: \n' + titles)


data = Data()
data.get_page()
data.get_movie_titles()
updater = Updater(token=bot_token)
# тут токен, который выдал вам Ботский Отец!
start_handler = CommandHandler('start', start)
movies_list_handler = CommandHandler('show_movies', show_movies)
book_ticket_handler = CommandHandler('book', book_ticket)
updater.dispatcher.add_handler(movies_list_handler)
updater.dispatcher.add_handler(start_handler)  # регистрируем в госреестре обработчиков
updater.dispatcher.add_handler(book_ticket_handler)
updater.start_polling()  # поехали!
