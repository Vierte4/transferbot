import configparser
import time
from threading import Thread

BOT_TOKEN = '5388513707:AAFzQLCby0XQxWzja84DTv4DtPT178coOEg'  # Токен бота

ADMINS = ['5169720405']  # id админов
USERS = []  # id пользователей

# ID каналов
channel_new = '-1001726042180'
channel_process = '-1001666292007'
channel_done = '-1001528763530'
channel_trash = '-1001679543941'

# Данные для подключения к базе данных
host = 'localhost'
port = 3306
user = 'root'
password = '26262866A'
db_name = 'main_db'

# Варианты перевода и получения по странам
russia_transfer = {'Сбербанк': ['RUB', 'Сбербанк'],
                   'Тинькофф': ['RUB', 'Тинькофф'],
                   'Альфа': ['RUB', 'Альфа'],
                   'Наличными в офисе в Москве': ['RUB',
                                                  'Наличными в офисе в Москве']
                   }

georgia_transfer = {
    'Доллары в офисе (Тбилиси, Костава 17)': ['USD', 'в офисе Тбилиси'],
    'Лари в офисе (Тбилиси, Костава 17)': ['GEL', 'в офисе Тбилиси'],
    'Лари на карту TBC': ['GEL', 'TBC'],
    'Лари на карту BOG': ['GEL', 'BOG'],
    'Лари на карту Credo': ['GEL', 'Credo'],
    'Лари на карту Liberty': ['GEL', 'Liberty']
    }

ukrain_transfer = {'Доллары на карту Ощадбанк': ['USD', 'Ощадбанк'],
                   'Доллары на карту Монобанк': ['USD', 'Монобанк'],
                   'Доллары на карту Приватбанк': ['USD', 'Приватбанк'],
                   'Гривны на карту Ощадбанк': ['UAH', 'Ощадбанк'],
                   'Гривны на карту Монобанк': ['UAH', 'Монобанк'],
                   'Гривны на карту Приватбанк': ['UAH', 'Приватбанк']
                   }

georgia_transfer_list = list(georgia_transfer.keys())
ukrain_transfer_list = list(ukrain_transfer.keys())
russia_transfer_list = list(russia_transfer.keys())

# Сообщение, полчаемое при запросе помощи
help_message = 'Контакты поддержки:\n' \
               'Telegram: @asad312\n' \
               'Телефон: +78005553535\n\n' \
               'Наши специалисты постараются ответить вам как можно быстрее!'

# Временные данные и курсы
temp = {}
courses = configparser.ConfigParser()


# Обновляем курсы каждую минуту
def update_courses():
    courses.read('data/courses.ini')



''''
Thread(target=update_courses, daemon=True).start()
'''
