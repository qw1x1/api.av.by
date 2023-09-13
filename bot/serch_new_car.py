import requests, time
from fake_useragent import UserAgent as Userr
from bs4 import BeautifulSoup as bs
from api.av1 import brand as brand_list
from api.av1 import Get_model_or_generations, Pars_info_id_file
from api.controls import get_user_id_on_procent
from api.models import *

class Get_new_car_list:
    '''
    Делает запрос на av.by, получет 25 новых авто, затем записывает их в список с дсктами.
    Вернёт список с диктами {'brand':brand_id, 'model':model_id, 'link':link_car, 'price': price_car, 'location': location, 'arg_price': arg_price, 'procent': procent, 'users': list[user_1, user_2]}
    ничего не принемает, нужно вызывать с интервалом в 10-15 мин
    '''
    def __init__(self):
        self.car = []
        self.f_user = Userr().random
        self.respons = None
    
    def get_model_id(self, brend_id, model):
        '''Вернет id модели по ее названию'''
        model_object = Get_model_or_generations(str(brand_list[brend_id]) +'/models')
        model_dict = model_object()[0]
        if model in model_dict:
            return model_dict[model]
        
    def get_generations_id(self, brend_id, model_id, generation_name):
        '''Вернет id поколения по ее названию'''
        generations_object = Get_model_or_generations(str(brend_id) +'/models/' + str(model_id)+ '/generations')
        generations_dict = generations_object()[0]
        if generation_name in generations_dict:
            return generations_dict[generation_name]
        return 0
    
    def get_car_name(self, lst):
        lst.reverse()
        if lst[0] == 'Рестайлнг' and len(lst) == 5:
            gen = f'{lst[2]} {lst[1]} Рестайлинг'
            mod = f'{lst[3]}'
            brand = f'{lst[4]}'
        elif lst[0] == 'мест' and len(lst) == 5:
            gen = str(lst[2]).replace(',', '')
            mod = f'{lst[3]}'
            brand = f'{lst[4]}'
        elif len(lst) == 3:
            gen = f'{lst[0]}'
            mod = f'{lst[1]}'
            brand = f'{lst[2]}'
        elif len(lst) == 6 and lst[0] == 'рестайлнг,':
            gen = f'{lst[3]} {lst[2]} {lst[1]} рестайлинг'
            mod = f'{lst[4]}'
            brand = f'{lst[5]}'
        elif len(lst) == 2:
            mod = f'{lst[0]}'
            brand = f'{lst[1]}'
            gen = 0
        else:
            gen = 0
            mod = 0
            brand = 0
        return brand, mod, gen

    def get_page(self): 
        respons_page = requests.get('https://cars.av.by/filter?', params={'condition[0]': 2, 'sort': 4}, headers={'user-agent': f'{self.f_user}'})
        if respons_page.status_code == 200:
            data_soup = bs(respons_page.text, 'lxml')
            self.respons = self.get_car_dict(data_soup)
        self.get_arg_price()

###############################################################################_____LOGIK_____###############################################################################

    def get_car_dict(self, data_soup):
        car_list = []
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            name_car = result.find('div', class_="listing-item__about").text.replace('VIN', '').replace('ТопОбъявление', '').replace('ТОПеПоднялось', '').replace('выше', '').replace('остальных', '').replace('в', '').replace('и', '').replace('собирает', '').replace('больше', '').replace('просмотроСпособы', '').replace('собрает', '').replace('ускореня', '').replace('продаж', '')
            link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            lst = self.get_car_name(name_car.split()[:6])
            print(lst)
            if lst[0] != 0:
                brand_id , model_id = brand_list[lst[0]], self.get_model_id(lst[0], lst[1])
                if brand_id and model_id:
                    car_list.append({'brand': brand_id, 'model': model_id, 'generation': self.get_generations_id(brand_id, model_id, lst[2]),  'link':link_car, 'price': price_car, 'arg_price': 0})
                else:
                    car_list.append({'brand': 0, 'model': 0, 'generation': 0, 'link':0, 'price': 0, 'arg_price': 0})

        self.car.append(car_list)
        return self.car[0]

    def get_average_market_value(self, car_list:list=[], count_page:int=0):
        count_items, total_price = 0, 0
        for i in range(count_page):
            for item in car_list[i]:
                count_items += 1
                total_price += item['price']
        return total_price/count_items

    def get_procent(self, price, arg_price):
        procent = 0
        if price < arg_price:
            procent = ((price / arg_price) * 100) - 100
        return abs(int(procent))

    def get_arg_price(self):
        ''' Находит среднерыночную стоимость авто в списке'''
        for item in self.respons:
            if item['model'] != None:
                dict_to_car = Pars_info_id_file(brand_id=item['brand'], model_id=item['model'], generations_id=item['generation'])
                params = dict_to_car()
                arg_price = self.get_average_market_value(params[0], params[1])
                item['arg_price'] = arg_price
                item['procent'] = self.get_procent(item['price'], item['arg_price'])
                item['users'] = self.record_users_if_dict(item['procent'])
                
    def record_users_if_dict(self, procent):
        user_list, users = [], get_user_id_on_procent(percent=procent)
        if len(users) >= 1:
            for user in users:
                user_list.append(user)
            return user_list

    def __call__(self):
        self.get_page()
        return self.respons

class Сheck_for_repeats():
    '''
    Убирает авто которые попали в список второй раз.
    Затем с интервалом обновляет данные.
    Обрабатывает все данные и отправляет найденые авто пользователям
    '''
    CAR_LIST = Get_new_car_list()

    def __init__(self):
        self.old_list = []
        self.new_list = []

    def get_not_repeats_list(self):
        self.new_list = self.CAR_LIST()
        for item in self.old_list:
            if item in self.new_list:
                self.new_list.remove(item)
        return self.new_list

    def get_old_list(self):
        self.old_list = self.get_not_repeats_list()

    def send_messeg_for_user(self, car_list):
        for item in car_list:
            for user in item['users']:
                print(user, item['link'])

    def __call__(self):
        while True:
            result_0 = self.get_old_list()
            result_2 = []
            if len(result_0) != 0:
                obj_1 = Create_list_respons(new_car = result_0)
                result_1 = obj_1()
                obj_2 = Serch_user_for_cars(result_1)
                result_2 = obj_2()
            if len(result_2) != 0:
                print(result_2)
                self.send_messeg_for_user(result_2)
            time.sleep(600)
            # 900 = 15min
            # 840 = 14min
            # 780 = 13min
            # 720 = 12min
            # 660 = 11min
            # 600 = 10min
            
    
# obj_3 = Сheck_for_repeats()
# res = obj_3()

obj_0 = Get_new_car_list()
res_0 = obj_0()
for i in res_0:
    print(i)
print(len(res_0))


















             
             
             
             
             
                  
             
             


