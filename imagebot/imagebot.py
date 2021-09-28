# Image-recognition-in-telegram-bot
# image recognition in telegram bot and translation into Russian

import logging, requests
from textblob import TextBlob
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = 'your_token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЭтот чат для распознования картинок.")

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    hi_blob = TextBlob(text)
    translates = hi_blob.translate(to='ru')
    
    return translates

@dp.message_handler(content_types=['photo'])
async def get_img_messages(message):
    id_image = message.photo[0].file_id
    url = f'https://api.telegram.org/bot{API_TOKEN}/getFile?file_id={message.photo[0].file_id}'
    file_path = requests.get(url).json()['result']['file_path']
    down_url = f'https://api.telegram.org/file/bot{API_TOKEN}/{file_path}'
    #print(file_path)

    r = requests.get(down_url)
    path = r'C:\Users\Elena\Desktop\Программирование\Picture\\' + str(id_image)
    with open(path, 'wb') as f:
        f.write(r.content)  

    await message.answer(ocr_core(path))
 
@dp.message_handler()
async def echo(message: types.Message):

    await message.answer("Загрузите картинку")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)