# **Telegram bot для получения новостей с сайта quote.rbc.ru**

В файле [newsbot](https://github.com/ElenaBalbukova/Telegram_bots/blob/newsbot/newsbot.py) написан код для получения новостей с сайта  quote.rbc.ru в телеграм канал.

### **Запуск**

**Для установки библиотек выполните команду:**
   ```python
   pip install -r requirements.txt
   ```

**В файле [newsbot](https://github.com/ElenaBalbukova/Telegram_bots/blob/newsbot/newsbot.py) укажите следующие строки кода:**
   
1. Здесь вы можете указать любой сайт, с которого хотите получать новости:
   ```
   url = 'https://quote.rbc.ru/?utm_source=topline'
   ```
2. id  из вашего телеграм канала:
    ```
    chat_id = "newsrbk0102"
    ```
3. token из вашего телеграм канала:
    ```
    bot_token = "your_token"
    ```
**Запустите Telegram bot командой:**
   ```python
   python3 newsbot.py
   ```