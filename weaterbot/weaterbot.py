import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

# перевод прогноза погоды на русский язык и получение данных с сайта: https://openweathermap.org
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('2ac7a22370d3dc875c742002b67f25c2', config_dict)
mgr = owm.weather_manager()

# получение сообщения с названием города и отправление прогноза погоды
bot = telebot.TeleBot("2042686170:AAEk-CIIZ6YlkexwcD3DzdJbhLBT_pGedbg") 

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    def town(gorod):
        
        town_exception = {"Нижний Новгород": "Нижнем Новгороде", "Ростов-на-Дону": "Ростове-на-Дону", "Набережные Челны": "Набережных Челных", "Астрахань": "Астрахани", "Тверь": "Твери", "Нижний Тагил": "Нижнем Тагиле", "Йошкар-Ола": "Йошкар-Оле", "Химки": "Химках", "Мытищи": "Мытищах", "Комсомольск-на-Амуре": "Комсомольск-на-Амуре", "Великий Новгород": "Великем Новгороде", "Керчь": "Керчи", "Ессентуки": "Ессентуках", "Евпатория": "Евпатории", "Новый Уренгой": "Новом Уренгое", "Казань": "Казани", "Старый Оскол": "Старом Осколе"
        }

        town = ((gorod).lower()).title()

        observation = mgr.weather_at_place(town)
        w = observation.weather

        # в функции учтены склонения городов с сайта: https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%D1%81_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC_%D0%B1%D0%BE%D0%BB%D0%B5%D0%B5_100_%D1%82%D1%8B%D1%81%D1%8F%D1%87_%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9
        if  town in town_exception:
            place = town_exception[town]
        elif town[ (len(town) -2) : len(town) ] in ["ый", "ий", "ой", "ое"]:
            place = town[:-2]  + 'ом'
        elif town[ len(town) - 1 ] == 'ы':    
            place = town[:-1]  + 'ах'
        elif town[ len(town) - 1 ] in ['и', 'о', 'э']:    
            place = town
        elif town[ len(town) - 1 ] == 'а':    
            place = town[:-1] + 'е'
        elif town[ len(town) - 1 ] == 'ь':    
            place = town[:-1] + 'е'
        else:
            place = town + 'е'

        temp = w.temperature('celsius')['temp']
        
        answer = "В городе " + place + " сейчас " + w.detailed_status + '\n'

        answer += "Температура в районе " + str( round(temp) ) + " градусов" + "\n"

        if temp < 10:
            answer += "На улице холодно, одевайся как танк!"
        elif temp < 20:
            answer += "На улице прозладно, одевайся теплее!"
        else:
            answer += "На улице тепло, одевай шорты!"

        return answer

    if __name__ == "__main__":
        town = town(message.text)

    bot.send_message(message.chat.id, town)

bot.polling( none_stop = True)