# **Telegram bot для распознования картинок**

В файле [imagebot](https://github.com/ElenaBalbukova/Telegram_bots/blob/imagebot/imagebot.py) написан код для распознования картинок с переводом на русский язык.

## **Запуск**

1. Установите программу [tesseract](https://github.com/tesseract-ocr/tesseract/releases/tag/4.1.1) для распознования картинок 

    Запустите программу:
    ```
    tesseract imagename outputbase [-l lang] [--oem ocrenginemode] [--psm pagesegmode] [configfiles...]
    ```
2. В файле [imagebot](https://github.com/ElenaBalbukova/Telegram_bots/blob/imagebot/imagebot.py) укажите:

    API_TOKEN:
    ```
    API_TOKEN = 'your_token'
    ```
    Путь до программы tesseract:
    ```
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```
    Путь куда будет сохраняться перевод:
    ```
    r'C:\Users\Elena\Desktop\Программирование\Picture\\' + str(id_image)
    ```
3. Запустите Telegram bot командой:
   ```
   python3 imagebot.py
   ```