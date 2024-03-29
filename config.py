import pickle
import gdown
from dotenv import load_dotenv, dotenv_values


load_dotenv()
config = dotenv_values(".env")

TELEGRAM_BOT_TOKEN= config['BOT_TOKEN'] 

WEB_SERVICE_NAME = 'https://test-tgbot-service.onrender.com'

START_BOT_TEXT = "Привет! Я - бот для распознавания различных овощей на фотографии. "\
    + "Отправь мне фотографию, если хочешь проверить мою работу."
    
ANSWER_ON_TEXT = "Извини, я не понимаю твое сообщение. Вышли фото, если хочешь проверить мою работу."

VEG_DICT = {
    0: 'Бобы (Bean)',
    1: 'Горькая тыква (Bitter Gourd)',
    2: 'Бутылочная тыква (Botter Gourd)',
    3: 'Баклажан (Brinjal)',
    4: 'Брокколи (Broccoli)',
    5: 'Капуста (Cabbage)',
    6: 'Стручковый перец (Capsicum)',
    7: 'Морковь (Carrot)',
    8: 'Цветная капуста (Cauliflower)',
    9: 'Огурец (Cucumber)',
    10: 'Папайя (Papaya)',
    11: 'Картофель (Potato)',
    12: 'Тыква (Pumpkin)',
    13: 'Редька (Radish)',
    14: 'Томат (Tomato)',
}

# для загрузки pickle-файла с обученной ML моделью
#url = 'https://drive.google.com/uc?id=14e4XLC96dYte0cF2XT8l9YMBSGb0JrXd'
url = 'https://drive.google.com/uc?id=15csxuXKm1MCuZUqASTbge1XY-rci3V8X'
output = 'LinearSVCBest.pkl'
gdown.download(url, output, quiet=False)
with open(output, "rb") as file:
    MODEL = pickle.load(file)

