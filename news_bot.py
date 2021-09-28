# News_rbk_telegram_channel
# Sending news to the telegram channel from the site "Rbc" investment section
from requests import get, post
from bs4 import BeautifulSoup

url = 'https://quote.rbc.ru/?utm_source=topline'
chat_id = "newsrbk0102"
bot_token = "your_token"


def get_news():
    response = get(url)
    resp_text = response.text

    soup = BeautifulSoup(resp_text, 'html.parser')
    soup.find("q-item__title")
    new_list_row = soup.find_all(class_="q-item js-load-item")

    news_list = []
    for i in new_list_row:      
        news_list.append(
            {
                'title':    i.find(class_="q-item__title").text.strip(), 
                'content':  i.find(class_="q-item__description").text.strip()
            }
        )
    print(news_list)
    return news_list


def send_message(dct):
    response = post(
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id=@{chat_id}&text={dct['title']}\n{dct['content']}"
    ) 
    print(response.text)    
[ send_message(i) for i in get_news() ]