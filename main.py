import asyncio
import logging
import time
#import pickle
#from io import BytesIO
#from PIL import Image
#from skimage import color
#from skimage.feature import hog
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from config_reader import config


TOKEN = config.bot_token.get_secret_value()
WEBHOOK_PATH =f"/bot/{TOKEN}"
RENDER_WEB_SERVICE_NAME = "test-tgbot-service"
WEBHOOK_URL = "https://" + RENDER_WEB_SERVICE_NAME + ".onrender.com" + WEBHOOK_PATH

# logging
logging.basicConfig(filemode='a', level=logging.INFO)
# объект бота
bot = Bot(token=TOKEN)
# диспетчер
dp = Dispatcher()

app = FastAPI()
'''
dp["veg_dict"] = {
    0: 'Bean',
    1: 'Bitter Gourd',
    2: 'Botter Gourd',
    3: 'Brinjal',
    4: 'Broccoli',
    5: 'Cabbage',
    6: 'Capsicum',
    7: 'Carrot',
    8: 'Cauliflower',
    9: 'Cucumber',
    10: 'Papaya',
    11: 'Potato',
    12: 'Pumpkin',
    13: 'Radish',
    14: 'Tomato',
}
with open("model.pkl", "rb") as file:
    dp["model"] = pickle.load(file)
'''
@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)

# хендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'Start: {user_id} {user_full_name} {time.asctime()}. Message: {message}')
    await message.answer("Hello!")
    
@dp.message()
async def main_handler(message: types.Message):
    try:
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        logging.info(f'Main: {user_id} {user_full_name} {time.asctime()}. Message: {message}')
        await message.reply("Hello world!")
    except:
        logging.info(f'Main: {user_id} {user_full_name} {time.asctime()}. Message: {message}. Error in main_handler')
        await message.reply("Something went wrong...")  
    
@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    #dp.set_current()
    Bot.set_current(bot)
    await dp.process_update(telegram_update)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.close()

@app.get("/")
def main_web_handler():
    return "Everything ok!"
'''
@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    bi = BytesIO()
    await bot.download(
        message.photo[-1],
        destination=bi
    )
    image = Image.open(bi)
    
    fd = hog(color.rgb2gray(image), 
        orientations=8, 
        pixels_per_cell=(16,16), 
        cells_per_block=(4, 4), 
        block_norm= 'L2'
    )
    fd = fd.reshape((1, fd.shape[0]))
    a = dp["model"].predict(fd)
    await message.answer("This is a {}".format(dp["veg_dict"][int(a[0])]))

'''   
#@dp.message(Command("info"))
#async def cmd_info(message: types.Message, started_at: str):
#    await message.answer("Бот предназначен для распознавания овощей на фотографиях")
'''   
@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")

@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")
'''
'''
# запуск процесса логгинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
'''
