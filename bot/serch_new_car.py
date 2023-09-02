from typing import Any
import requests
from fake_useragent import UserAgent as Userr
from bs4 import BeautifulSoup as bs
from api.av1 import brand, Get_model, Pars_info_id_file
from api.controls import get_request
from api.models import *

test_list = [{'brand': 1238, 'model': 1262, 'link': 'https://cars.av.by/volvo/xc70/105570262', 'price': 22900, 'location': 'Лида', 'arg_price': 15669.1875},
             {'brand': 1216, 'model': 1974, 'link': 'https://cars.av.by/volkswagen/tiguan/105570332', 'price': 11500, 'location': 'Жлобин', 'arg_price': 24082.986270022884},
             {'brand': 1039, 'model': None, 'link': 'https://cars.av.by/renault/grand-scenic/105463046', 'price': 22600, 'location': 'Минск', 'arg_price': 0},
             {'brand': 683, 'model': 820, 'link': 'https://cars.av.by/mercedes-benz/viano/105627663', 'price': 22999, 'location': 'Минск', 'arg_price': 17434.843137254902},
             {'brand': 43, 'model': 181, 'link': 'https://cars.av.by/citroen/c5/105435652', 'price': 5450, 'location': 'Минск', 'arg_price': 6693.4951768488745},
             {'brand': 43, 'model': 178, 'link': 'https://cars.av.by/citroen/berlingo/104885011', 'price': 11000, 'location': 'Гродно', 'arg_price': 7279.571428571428},
             {'brand': 6, 'model': 5812, 'link': 'https://cars.av.by/audi/a8/105035770', 'price': 18950, 'location': 'Жлобин', 'arg_price': 22360.14619883041},
             {'brand': 892, 'model': 2306, 'link': 'https://cars.av.by/nissan/leaf/105435450', 'price': 19500, 'location': 'Минск', 'arg_price': 14557.008547008547},
             {'brand': 1216, 'model': 1974, 'link': 'https://cars.av.by/volkswagen/tiguan/105409480', 'price': 27200, 'location': 'Минск', 'arg_price': 24082.986270022884},
             {'brand': 1238, 'model': 1717, 'link': 'https://cars.av.by/volvo/v90-cross-country/105409190', 'price': 39500, 'location': 'Минск', 'arg_price': 27264.36842105263},
             {'brand': 2012, 'model': None, 'link': 'https://cars.av.by/geely/coolray/105406987', 'price': 19990, 'location': 'Минск', 'arg_price': 0},
             {'brand': 433, 'model': 5384, 'link': 'https://cars.av.by/hyundai/creta/105406486', 'price': 22200, 'location': 'Минск', 'arg_price': 20258.721739130433},
             {'brand': 683, 'model': 5897, 'link': 'https://cars.av.by/mercedes-benz/s-klass-amg/105399371', 'price': 72500, 'location': 'Минск', 'arg_price': 24343.136},
             {'brand': 2012, 'model': None, 'link': 'https://cars.av.by/geely/emgrand-x7/105363797', 'price': 22200, 'location': 'Минск', 'arg_price': 0},
             {'brand': 8, 'model': 5867, 'link': 'https://cars.av.by/bmw/x5/105363652', 'price': 46900, 'location': 'Минск', 'arg_price': 41081.10339943343},
             {'brand': 433, 'model': 5384, 'link': 'https://cars.av.by/hyundai/creta/105339165', 'price': 21200, 'location': 'Минск', 'arg_price': 20258.721739130433},
             {'brand': 834, 'model': 875, 'link': 'https://cars.av.by/mitsubishi/outlander/105319901', 'price': 24700, 'location': 'Минск', 'arg_price': 16399.98367346939},
             {'brand': 526, 'model': 5291, 'link': 'https://cars.av.by/jaguar/f-pace/105259699', 'price': 38500, 'location': 'Минск', 'arg_price': 38539.781818181815},
             {'brand': 892, 'model': 1768, 'link': 'https://cars.av.by/nissan/qashqai/105249731', 'price': 19990, 'location': 'Минск', 'arg_price': 17522.932084309134},
             {'brand': 2012, 'model': None, 'link': 'https://cars.av.by/geely/coolray/105249600', 'price': 23400, 'location': 'Минск', 'arg_price': 0},
             {'brand': 1506, 'model': 2570, 'link': 'https://cars.av.by/buick/encore/105207739', 'price': 15300, 'location': 'Минск', 'arg_price': 15741.606557377048},
             {'brand': 2012, 'model': 5846, 'link': 'https://cars.av.by/geely/atlas-pro/105167592', 'price': 27700, 'location': 'Минск', 'arg_price': 20239.297297297297},
             {'brand': 1485, 'model': 1493, 'link': 'https://cars.av.by/porsche/cayenne/105159545', 'price': 74500, 'location': 'Минск', 'arg_price': 39384.88636363636},
             {'brand': 8, 'model': None, 'link': 'https://cars.av.by/bmw/ix/105153728', 'price': 88800, 'location': 'Минск', 'arg_price': 0},
             {'brand': 6, 'model': 5811, 'link': 'https://cars.av.by/audi/a6/105153155', 'price': 30200, 'location': 'Минск', 'arg_price': 15412.228003784296}]

class Get_new_car_list:
    '''
    Вернёт список с диктами {'brand':brand_id, 'model':model_id, 'link':link_car, 'price': price_car, 'location': location, 'arg_price': arg_price}
    ничего не принемает, нужно вызывать с интервалом в 10-15 мин
    '''
    def __init__(self):
        self.car = []
        self.f_user = Userr().random
        self.respons = None
    
    def get_model_id(self, brend_id, model):
        model_object = Get_model()
        model_dict = model_object.get_data_select_car(str(brand[brend_id]) +'/models')
        if model in model_dict:
            return model_dict[model]

    def get_car_dict(self, data_soup):
        car_list = []
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            name_car = result.find('div', class_="listing-item__about").text
            link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

            lst = name_car.split() 
            if lst[0] in brand:
                car_list.append({'brand':brand[lst[0]], 'model':self.get_model_id(lst[0], lst[1]), 'link':link_car, 'price': price_car, 'location': location, 'arg_price': 0})
        self.car.append(car_list)
        return self.car[0]

    def get_page(self): 
        respons_page = requests.get('https://cars.av.by/filter?', params={'condition[0]': 2, 'sort': 4}, headers={'user-agent': f'{self.f_user}'})
        if respons_page.status_code == 200:
            data_soup = bs(respons_page.text, 'lxml')
            self.respons = self.get_car_dict(data_soup)
        self.get_arg_price()

    def get_average_market_value(self, car_list:list=[], count_page:int=0):
        count_items, total_price = 0, 0
        for i in range(count_page):
            for item in car_list[i]:
                count_items += 1
                total_price += item['price']
        return total_price/count_items

    def get_arg_price(self): # берет список машин, делает запрос по их brand_id и model_id, и находит их среднерыночную стоимость
        for item in self.respons:
            if item['model'] != None:
                dict_to_car = Pars_info_id_file(brand_id=item['brand'], model_id=item['model'])
                params = dict_to_car()
                arg_price = self.get_average_market_value(params[0], params[1])
                item['arg_price'] = arg_price

    def __call__(self):
        self.get_page()
        return self.respons

class Create_list_respons():
    '''
    На вход передаем список из класса Get_new_car_list
    Вернёт список с диктами {'brand':brand_id, 'model':model_id, 'link':link_car, 'price': price_car, 'location': location, 'arg_price': arg_price, 'procent': procent}
    '''
    def __init__(self, new_car:list=[]):
        self.new_car = new_car
        self.result_list = []

    @staticmethod
    def get_procent(price, arg_price):
        procent = 0
        if price < arg_price:
            procent = ((price / arg_price) * 100) - 100
        return abs(int(procent))

    def cek_car_in_user(self):
        for car in self.new_car:
            procent = self.get_procent(car['price'], car['arg_price'])
            if procent != 0:
                car['procent'] = procent
                self.result_list.append(car)
    
    def __call__(self):
        self.cek_car_in_user()
        return self.result_list

class Serch_user_for_cars():
    '''
    На вход передаем список из класса Create_list_respons
    Вернёт список с диктами {'brand':brand_id, 'model':model_id, 'link':link_car, 'price': price_car, 'location': location, 'arg_price': arg_price, 'procent': procent, 'users': list[user_1, user_2]}
    '''
    def __init__(self, car_list:list = []):
        self.car_list = car_list
        self.result_list  = []

    @staticmethod
    def serch_users(brand_id=0, model_id=0, percent=0):
        return get_request(brand_id=brand_id, model_id=model_id, percent=percent)

    def record_users_if_dict(self):
        for item in self.car_list:
            users = self.serch_users(brand_id=item['brand'], model_id=item['model'], percent=item['procent'])
            user_list = []
            if len(users) >= 1:
                for user in users:
                   user_list.append(user)
                item['users'] = user_list

    def __call__(self):
        self.record_users_if_dict()
        return self.car_list





def forr(list):
    for i in list:
        print(i)







# obj = Get_new_car_list()
# result = obj()
# forr(result)


# with db:
#     requestt = get_request(brand_id=1, model_id=3, percent=55)
#     print()
#     for item in requestt:
#         print(item)


# obj_1 = Create_list_respons(new_car = test_list)
# result_1 = obj_1()
# obj_2 = Serch_user_for_cars(result_1)
# result_2 = obj_2()

# forr(result_1)
# print()
# forr(result_2)



#######################################################################################################################################################################################


# old_list = [{'brand': 1238, 'model': 1262, 'link': 'https://cars.av.by/volvo/xc70/105570262', 'price': 22900, 'location': 'Лида', 'arg_price': 15669.1875},
#              {'brand': 1216, 'model': 1974, 'link': 'https://cars.av.by/volkswagen/tiguan/105570332', 'price': 11500, 'location': 'Жлобин', 'arg_price': 24082.986270022884},
#              {'brand': 683, 'model': 820, 'link': 'https://cars.av.by/mercedes-benz/viano/105627663', 'price': 22999, 'location': 'Минск', 'arg_price': 17434.843137254902},
#              {'brand': 43, 'model': 181, 'link': 'https://cars.av.by/citroen/c5/105435652', 'price': 5450, 'location': 'Минск', 'arg_price': 6693.4951768488745},
#              {'brand': 43, 'model': 178, 'link': 'https://cars.av.by/citroen/berlingo/104885011', 'price': 11000, 'location': 'Гродно', 'arg_price': 7279.571428571428},
#              {'brand': 6, 'model': 5812, 'link': 'https://cars.av.by/audi/a8/105035770', 'price': 18950, 'location': 'Жлобин', 'arg_price': 22360.14619883041},
#              {'brand': 892, 'model': 2306, 'link': 'https://cars.av.by/nissan/leaf/105435450', 'price': 19500, 'location': 'Минск', 'arg_price': 14557.008547008547},
#              {'brand': 1216, 'model': 1974, 'link': 'https://cars.av.by/volkswagen/tiguan/105409480', 'price': 27200, 'location': 'Минск', 'arg_price': 24082.986270022884},
#              {'brand': 1238, 'model': 1717, 'link': 'https://cars.av.by/volvo/v90-cross-country/105409190', 'price': 39500, 'location': 'Минск', 'arg_price': 27264.36842105263},
#              {'brand': 433, 'model': 5384, 'link': 'https://cars.av.by/hyundai/creta/105406486', 'price': 22200, 'location': 'Минск', 'arg_price': 20258.721739130433},
#              {'brand': 683, 'model': 5897, 'link': 'https://cars.av.by/mercedes-benz/s-klass-amg/105399371', 'price': 72500, 'location': 'Минск', 'arg_price': 24343.136},
#              {'brand': 8, 'model': 5867, 'link': 'https://cars.av.by/bmw/x5/105363652', 'price': 46900, 'location': 'Минск', 'arg_price': 41081.10339943343},
#              {'brand': 433, 'model': 5384, 'link': 'https://cars.av.by/hyundai/creta/105339165', 'price': 21200, 'location': 'Минск', 'arg_price': 20258.721739130433},
#              {'brand': 834, 'model': 875, 'link': 'https://cars.av.by/mitsubishi/outlander/105319901', 'price': 24700, 'location': 'Минск', 'arg_price': 16399.98367346939},
#              {'brand': 526, 'model': 5291, 'link': 'https://cars.av.by/jaguar/f-pace/105259699', 'price': 38500, 'location': 'Минск', 'arg_price': 38539.781818181815},
#              {'brand': 892, 'model': 1768, 'link': 'https://cars.av.by/nissan/qashqai/105249731', 'price': 19990, 'location': 'Минск', 'arg_price': 17522.932084309134},
#              {'brand': 1506, 'model': 2570, 'link': 'https://cars.av.by/buick/encore/105207739', 'price': 15300, 'location': 'Минск', 'arg_price': 15741.606557377048},
#              {'brand': 2012, 'model': 5846, 'link': 'https://cars.av.by/geely/atlas-pro/105167592', 'price': 27700, 'location': 'Минск', 'arg_price': 20239.297297297297},
#              {'brand': 1485, 'model': 1493, 'link': 'https://cars.av.by/porsche/cayenne/105159545', 'price': 74500, 'location': 'Минск', 'arg_price': 39384.88636363636},
#              {'brand': 6, 'model': 5811, 'link': 'https://cars.av.by/audi/a6/105153155', 'price': 30200, 'location': 'Минск', 'arg_price': 15412.228003784296}]


# def get_list(test_list):
#     return test_list


# def check_for_repeats(old_list):
#     new_list = get_list(test_list)
#     for item in old_list:
#         if item in new_list:
#             new_list.remove(item)
#     return new_list

# lists = check_for_repeats(old_list)
# forr(lists[1])
import time

class Сheck_for_repeats():
    CAR_LIST = Get_new_car_list()

    def __init__(self):
        self.old_list = [0,1,2,3,4]
        self.new_list = [0,1,2,3,4,5,6,7,8,9]
            
    def get_not_repeats_list(self):
        # self.new_list = self.CAR_LIST()
        for item in self.old_list:
            if item in self.new_list:
                self.new_list.remove(item)
        return self.new_list

    def run(self):
        self.old_list = self.get_not_repeats_list()
    
    def __call__(self):
        while True:
            self.run()
            forr(self.new_list)
            time.sleep(5)
            
        
        
    
obj_3 = Сheck_for_repeats()
res = obj_3()
# forr(res)

















             
             
             
             
             
                  
             
             


