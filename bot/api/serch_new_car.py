import requests, asyncio, time
from fake_useragent import UserAgent as Userr
from bs4 import BeautifulSoup as bs
from api.controls import get_user_id_on_procent, create_respons, get_respons_list
from aiogram import Bot

bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')

async def send_msg(id, message):
    await bot.send_message(id, message) 

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
        except Exception:
            time.sleep(60)
            self.get_page()

        if respons_page.status_code == 200:
            self.respons = self.get_car_dict(bs(respons_page.text, 'lxml'))
        else:
            time.sleep(60)
            self.get_page()
        self.get_arg_price()

    def get_car_dict(self, data_soup):
        links = get_respons_list()
        car_list = []
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            link = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            price = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            location = result.find('div', class_="listing-item__info").text.replace('только что', '').replace('минуту назад', '').replace('минуты назад', '').replace('минут назад', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace(' ', '')
            
            if str(link) not in links:
                car_list.append({'link':link, 'price': price, 'location': location,})
                create_respons(link=link)             
            else:
                continue
        return car_list
    
    def pars_page(self, link):
        respons_page = requests.get(link, headers={'user-agent': f'{self.f_user}'})
        if respons_page.status_code == 200:
            data_soup = bs(respons_page.text, 'lxml')
            return self.mid_price(data_soup)
        else:
            time.sleep(60)
            self.pars_page(link)

    def mid_price(self, data_soup):       
        total = ''
        mid_price = str(data_soup.find(class_='featured__price-value'))
        if mid_price != None:
            for item in mid_price:
                if item in '1234567890':
                    total += item
        if total != '':
            return int(total)
        return 300
    
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
        user_list, users = [], get_user_id_on_procent(procent, location)
        if len(users) >= 1:
            for user in users:
                user_list.append(str(user))
            return user_list
    
    def __call__(self):
        self.get_page()
        print(self.respons)############################################
        return self.respons
    
async def main():
    obj = Get_new_car_list()
    while True:
        car_list = obj()
        for item in car_list:
            if type(item['users']) == list:
                for user in item['users']:
                    # В этом месте проверям есть ли у пользователя подписка, если ее нет меняем статус подписки в бд 
                    message = 'Средняя стоимость авто: ' + str(item['arg_price']) + '$' + '\n' + 'Процент отклонения от рынка: ' + str(item['procent']) + '%' + '\n' + str(item['link'])
                    await send_msg(user, message)

if __name__ ==  '__main__':
    asyncio.run(main())   