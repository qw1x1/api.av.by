import requests, time
from fake_useragent import UserAgent as Userr
from bs4 import BeautifulSoup as bs
from av1 import brand as brand_list
from av1 import Get_model_or_generations, Pars_info_id_file
from controls import get_user_id_on_procent
from models import *

class Get_new_car_list:
    '''
    Делает запрос на av.by, получет 25 новых авто, затем записывает их в список с дсктами.
    Вернёт список с диктами {'brand':brand_id, 'model':model_id, 'link':link_car, 'price': price_car, 'location': location, 'arg_price': arg_price, 'procent': procent, 'users': list[user_1, user_2]}
    ничего не принемает, нужно вызывать с интервалом в 10-15 мин
    '''
    ID_CAR = [5076, 1310, 10094, 1551, 2894, 2345, 2051, 5252, 5032, 1464, 5019, 1279, 0]
    CAR_NAME = ["Lada", "Богдан", "ГАЗ", "ЕрАЗ", "ЗАЗ", "ИЖ", "ЛуАЗ", "Москвич", "РАФ", "ТагАЗ", "УАЗ", "Эксклюзив", "Shanghai", "Great", "GAC", "Dongfeng", "Aston"]

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
        if lst[0] in self.CAR_NAME:
            return 0, 0, 0
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
        try:
            respons_page = requests.get('https://cars.av.by/filter?', params={'condition[0]': 2, 'sort': 4}, headers={'user-agent': f'{self.f_user}'})
        except ConnectionError:
            return 0
        if respons_page.status_code == 200:
            self.respons = self.get_car_dict(bs(respons_page.text, 'lxml'))
        self.get_arg_price()

###############################################################################_____LOGIK_____###############################################################################

    def get_car_dict(self, data_soup):
        car_list = []
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            name = result.find('div', class_="listing-item__about").text.replace('VIN', '').replace('ТопОбъявление', '').replace('ТОПеПоднялось', '').replace('выше', '').replace('остальных', '').replace('в', '').replace('и', '').replace('собирает', '').replace('больше', '').replace('просмотроСпособы', '').replace('собрает', '').replace('ускореня', '').replace('продаж', '')
            link = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            price = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            lst = self.get_car_name(name.split()[:6])
            if lst[0] != 0:
                brand_id , model_id = brand_list[lst[0]], self.get_model_id(lst[0], lst[1])
                if brand_id and model_id:
                    car_list.append({'brand': brand_id, 'model': model_id, 'generation': self.get_generations_id(brand_id, model_id, lst[2]),  'link':link, 'price': price, 'arg_price': 0})
                else:
                    car_list.append({'brand': 0, 'model': None, 'generation': 0, 'link': 0, 'price': 0, 'arg_price': 0, 'users': 0})

        self.car.append(car_list)
        return self.car[0]

    def get_average_market_value(self, car_list:list=[], count_page:int=0):
        count_items, total_price = 0, 0
        for i in range(count_page):
            for item in car_list[i]:
                count_items += 1
                total_price += item['price']
        if count_items == 0:
            count_items = 1
        return total_price/count_items

    def get_procent(self, price, arg_price):
        procent = 0
        if price < arg_price:
            procent = ((price / arg_price) * 100) - 100
        return abs(int(procent))

    def get_arg_price(self):
        ''' Находит среднерыночную стоимость авто в списке'''
        for item in self.respons:
            if item['model'] != None or item['model'] != 0 and item['brand'] not in self.ID_CAR:
                # в dict_to_car попадают brand_id=0, model_id=0, generations_id=0, изза этого все идет по пизде
                print(item['brand'], item['model'], item['generation'])
                dict_to_car = Pars_info_id_file(brand_id=item['brand'], model_id=item['model'], generations_id=item['generation'])
                params = dict_to_car()
                if params[1] == 0 and params[0] == 0:
                    item['arg_price'], item['procent'], item['users'] = 0, 0, 0
                else:
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
    
    # НЕ ЮЗАЕТЬСЯ!!?
    def del_repit(self):
        for item in self.respons:
            if item['users'] == None:
                self.respons.remove(item)

    def __call__(self):
        self.get_page()
        return self.respons

class Сheck_for_repeats():
    '''
    Убирает авто которые попали в список второй раз.
    Затем с интервалом обновляет данные.
    Обрабатывает все данные и отправляет найденые авто пользователям
    '''

    def __init__(self):
        self.old_list = []

    def get_not_repeats_list(self, new_list):
        
        for item in self.old_list:
            if item in new_list:
                new_list.remove(item)
        return new_list

    def get_old_list(self):
        obj = Get_new_car_list()
        new_list = obj()
        self.old_list = self.get_not_repeats_list(new_list)
        return self.old_list

    def send_messeg_for_user(self, car_list):
        for item in car_list:
            if type(item['users']) == list:
                for user in item['users']:
                    print(user, item['link'], item['procent'], item['price'])

    def __call__(self):
        while True:
            result_0 = self.get_old_list()
            if len(result_0) != 0:
                self.send_messeg_for_user(result_0)
            
obj_3 = Сheck_for_repeats()
obj_3()

# obj_0 = Get_new_car_list()
# res_0 = obj_0()
# for i in res_0:
#     print(i)
# print(len(res_0))
# while True:
#     obj = Get_new_car_list()
#     print(obj)
#     result = obj()
#     for item in result:
#             if type(item['users']) == list:
#                 for user in item['users']:
#                     print(user, item['link'], item['procent'], item['price'])
#     print(time.ctime(time.time()))

    # time.sleep(300)


# add_procent_user(11, 44)














             
             
             
             
             
                  
             
             


