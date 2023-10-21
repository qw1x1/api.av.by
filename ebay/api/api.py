import requests, asyncio
from time import sleep, perf_counter
from threading import Thread
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
from controls import *

class Get_link_list(): # -> link
    '''
    Принимет на вход поисковый link и возвращает список ссылок с товарами
    '''
    def __init__(self, link):
        self.link = link
        self.old_sherch_data = []   
        self.user = User()

    def get_not_repeats_list(self, new_list):
        for item in self.old_sherch_data:
            if item in new_list:
                new_list.remove(item)
        return new_list

    def get_old_list(self):
        new_list = self.get_respons_list(self.link)
        self.old_sherch_data = self.get_not_repeats_list(new_list)
        return self.old_sherch_data
            
    def get_respons_list(self, link):
        links = []
        try:
            respons_page = requests.get(link, headers={'user-agent': f'{self.user}'})
            if respons_page.status_code == 200:
                data_soup = bs(respons_page.text, 'lxml')
                for item in data_soup.find("div", {"id": "srchrslt-content"}).find_all('a', class_="ellipsis"):
                    links.append(item.get('href'))
                if len(links) > 25:
                    return links[2:]
                return links
            return 0
        except ConnectionError:
            return 0

    def __call__(self):
        while True:
            return self.get_old_list()

def get_list_lincs_for_serch(link):
    obj = Get_link_list(link)
    obj1 = obj()
    print(obj1[0])


def main_loop():
    users = list(get_users())

    for user in users:
        sherch_data, threads = get_sefch_data_list(str(user)), []
        # 
        start_time = perf_counter()
        # 
        
        for item in sherch_data:
            thread = Thread(target=get_list_lincs_for_serch, args=(item['link'],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # 
        end_time = perf_counter()
        # 
        print(f'Выполнение заняло {end_time- start_time: 0.2f} секунд.')

# main_loop()