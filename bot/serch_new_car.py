import requests
from fake_useragent import UserAgent as Userr
from bs4 import BeautifulSoup as bs
from api.av1 import brand, Get_model, Pars_info_id_file
from api.controls import Control_db, get_request
from api.models import *

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



# obj = Get_new_car_list()
# result = obj()
# for car in result:
#     print(car)




# with db:
#     requestt = get_request(brand_id=1, model_id=3, percent=55)
#     print()
#     for item in requestt:
#         print(item)