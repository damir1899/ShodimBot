import requests
from bs4 import BeautifulSoup

from core.config import PARS_DOMAIN, PARS_URL, HEADERS
from core.database import add_information_places

def get_html(URL, HEADERS):
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        return f'Error: {response.status_code}'

def processing(response):
    soup = BeautifulSoup(response, 'lxml').find(
        'div', {'class': 'impression-items'}).find_all(
        'div', {'class': 'impression-card'})
        
    for item in soup:
        category = item.get('data-category')
        title = str(item.get('data-title')).replace("'", "")
        information = str(item.find('div', {'class': 'impression-card-info'}).text).strip()
        url = item.find('a', {'class': 'impression-card-title'}).get('href')
        photo = PARS_DOMAIN + str(item.find('div', {'class': 'impression-card-image'}).find('img').get("src"))
        add_information_places(category, title, information, url, photo)
        
        

def start_parser():
    for page in range(1, 119):
        res = get_html(PARS_URL + str(page), HEADERS)
        processing(res)
        print('Страниц готова:', page)
        
start_parser()