import requests
from fake_useragent import UserAgent as Userr
from bs4 import BeautifulSoup as bs
from controls import get_user_id_on_procent, create_respons, get_respons_list, set_cars

class Get_new_car_list:
    '''
    Вернёт список с диктами {'link':link_car, 'price': price_car, 'location': location, 'arg_price': arg_price, 'procent': procent, 'users': list[user_1, user_2]}
    '''

    def __init__(self):
        self.f_user = Userr().random
        self.respons = None
    
    def get_page(self):
        try:
            respons_page = requests.get('https://cars.av.by/filter?', params={'condition[0]': 2, 'sort': 4}, headers={'user-agent': f'{self.f_user}'})
        except ConnectionError:
            return 0
        if respons_page.status_code == 200:
            self.respons = self.get_car_dict(bs(respons_page.text, 'lxml'))
        self.get_arg_price()

    def get_car_dict(self, data_soup):
        links = get_respons_list()
        car_list = []
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            link = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            price = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            location = result.find('div', class_="listing-item__info").text.replace('только что', '').replace('минуту назад', '').replace('минуты назад', '').replace('минут назад', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
            
            if str(link) not in links:
                car_list.append({'link':link, 'price': price, 'location': location, 'arg_price': 0})
                create_respons(link=link)             
            else:
                continue
        return car_list
    
    def pars_page(self, link):
        respons_page = requests.get(link, headers={'user-agent': f'{self.f_user}'})
        if respons_page.status_code == 200:
            data_soup = bs(respons_page.text, 'lxml')
            return self.mid_price( data_soup)
        return 0

    def mid_price(self, data_soup):       
        total = ''
        try:
            mid_price = data_soup.find(class_='featured__price-value').text
        except AttributeError:
            mid_price = data_soup.find(class_='card__price-secondary').text
        
        for item in mid_price:
            if item in '1234567890':
                total += item
        return int(total)

    def get_procent(self, price, arg_price):
        procent = 0
        if price < arg_price:
            procent = ((price / arg_price) * 100) - 100
        return abs(int(procent))

    def get_arg_price(self):
        ''' Находит среднерыночную стоимость авто в списке'''
        for item in self.respons:
            item['arg_price'] = self.pars_page(item['link'])
            item['procent'] = self.get_procent(item['price'], item['arg_price'])
            item['users'] = self.record_users_if_dict(item['procent'], item['location'])
                
    def record_users_if_dict(self, procent, location):
        user_list, users = [], get_user_id_on_procent(percent=procent, location=location)
        if len(users) >= 1:
            for user in users:
                user_list.append(str(user))
            return user_list
    
    def __call__(self):
        self.get_page()
        return self.respons

obj = Get_new_car_list()
while True:
    car_list = obj()
    for item in car_list:
        if type(item['users']) == list:
            print(type(item['users']), item['link'], item['procent'], item['price'], item['users'], item['location'])
            set_cars(link=item['link'], users=list(item['users']))
            # print()
            