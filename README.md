# **Telegram bot для получения прогноза погоды**

В файле [weaterbot](https://github.com/ElenaBalbukova/Telegram_bots/blob/weaterbot/weaterbot.py) написан код эхобота, который присылает прогноз погоды, ссылочка на бота [здесь](https://t.me/PogodaFamilyBot). Пользователь отправляет боту город и получает в ответ состояние погоды, температуру и рекомендации как одеться.

## **Запуск**

1. Для установки библиотек выполните команду:
   ```
   pip install -r requirements.txt
   ```
2. В файле [weaterbot](https://github.com/ElenaBalbukova/Telegram_bots/blob/weaterbot/weaterbot.py) укажите API keys и API token:
   ```python
   owm = OWM('API keys', config_dict)
   ```
    ```python
   bot = telebot.TeleBot("API token") 
   ```
3.1. Для запуска Telegram bot на локальном компьютере выполните команду:
   ```python
   python3 weater_bot.py
   ```
3.2. Для запуска Telegram bot на хостинге heroku выполните команду:
   ```python
   heroku ps:scale worker=1
   ```

### **Тесткейс**

Для проверки работы кода для городов с [сайта](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%D1%81_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC_%D0%B1%D0%BE%D0%BB%D0%B5%D0%B5_100_%D1%82%D1%8B%D1%81%D1%8F%D1%87_%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9) запустите:
```python
python3 test_town.py
```

   