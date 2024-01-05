import numpy as np
from io import BytesIO
from PIL import Image
from skimage import color
from skimage.feature import hog
from aiogram import Dispatcher, Bot, types, executor
import config 


bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(config.START_BOT_TEXT)
    
@dp.message_handler(content_types=["text"])
async def answer_on_text(message: types.Message):
    await message.reply(config.ANSWER_ON_TEXT)
    
@dp.message_handler(content_types=['photo'])
async def photo_id(message):
    io = BytesIO()
    await message.photo[-1].download(destination_file=io)
    image = Image.open(io)
    fd = hog(color.rgb2gray(image), 
        orientations=8, 
        pixels_per_cell=(16,16), 
        cells_per_block=(4, 4), 
        block_norm= 'L2'
    )
    fd = fd.reshape((1, fd.shape[0]))
    
    a = config.MODEL.predict(fd)
    await message.answer('Овощ на фото - {}'.format(config.VEG_DICT[int(a[0])]))
    
    #await message.answer('photo rendered')

