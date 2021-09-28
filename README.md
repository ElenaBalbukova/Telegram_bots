# **Telegram bot для получения новостей с сайта quote.rbc.ru**

В файле [news_bot](https://github.com/ElenaBalbukova/Telegram_bots/blob/master/News_rbk_telegram_channel.py) написан код получения нововстей с сайта  quote.rbc.ru в телеграм канал.

### **Запуск**

В файле [news_bot](https://github.com/ElenaBalbukova/Telegram_bots/blob/master/News_rbk_telegram_channel.py) укажите следующие строки кода:
   
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
4. Запустите Telegram bot командой:
   ```python
   python3 News_rbk_telegram_channel.py
   ```