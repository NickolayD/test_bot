import pickle
from dotenv import load_dotenv, dotenv_values


load_dotenv()
config = dotenv_values(".env")

TELEGRAM_BOT_TOKEN= config['BOT_TOKEN'] 

NGROK_TUNNEL_URL = 'https://238f-88-206-25-29.ngrok-free.app'

START_BOT_TEXT = "Привет! Я - бот для распознавания различных овощей на фотографии."\
    + "Отправь мне фотографию, если хочешь проверить мою работу."
    
ANSWER_ON_TEXT = "Извини, я не понимаю твое сообщение. Вышли фото, если хочешь проверить мою работу."

VEG_DICT = {
    0: 'Бобы(Bean)',
    1: 'Горькая тыква(Bitter Gourd)',
    2: 'Бутылочная тыква(Botter Gourd)',
    3: 'Баклажан(Brinjal)',
    4: 'Брокколи(Broccoli)',
    5: 'Капуста(Cabbage)',
    6: 'Стручковый перец(Capsicum)',
    7: 'Морковь(Carrot)',
    8: 'Цветная капуста(Cauliflower)',
    9: 'Огурец(Cucumber)',
    10: 'Папайя(Papaya)',
    11: 'Картофель(Potato)',
    12: 'Тыква(Pumpkin)',
    13: 'Редька(Radish)',
    14: 'Томат(Tomato)',
}
'''
with open("model.pkl", "rb") as file:
    MODEL = pickle.load(file)
'''