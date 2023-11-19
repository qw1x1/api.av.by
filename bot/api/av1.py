import requests, json, math
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
from bot.settings import BRAND as brand
from bot.settings import REVERS_BRAND as revers_brand
from bot.settings import CITY_IN_REGION as REGION

class Get_model_or_generations():
    '''
    Get_model_or_generations(str(brend_id) +'/models') Это для того чтоб получить дикт с модетлями

    '''
    def __init__(self, params, user_id=0):
        self.user = User().random 
        self.params = params
        self.dikt, self.revers_dikt = {}, {}
        self.data = None
        self.user = user_id

    def get_revevs_name(self):
        for i in range(len(self.data)):
            self.dikt[self.data[i]['name']] = self.data[i]['id']
            self.revers_dikt[self.data[i]['id']] = self.data[i]['name']

    def get_data_select_car(self):
        self.dikt.clear()
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/' + self.params, headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            self.data = json.loads(respons_list.text)
            self.get_revevs_name()

    def __call__(self):
        self.get_data_select_car()
        return self.dikt, self.revers_dikt
    
class Pars_info_id_file(): # -> car_list
    def __init__(self, brand_id=1, model_id=3, generations_id=0):
        self.brand_id, self.model_id, self.generations_id = brand_id, model_id, generations_id
        self.user = User().random
        self.car = []
        self.count_page=0

    def get_car_dict(self, data_soup, param=0): # -> Return list for car
        car_list, respons_list = [], []
        try:
            if param == 1:
                count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))
                respons_list = [count_ad]
        except AttributeError:
            respons_list = [0]
            return respons_list
        
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            
            car_list.append({'link':link_car,'price': price_car})
        self.car.append(car_list)
        return  respons_list

    def get_page(self):
        if self.brand_id == 0 or self.model_id == 0:
            return 0
        params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'brands[0][generation]': self.generations_id, 'condition[0]': 2, 'sort': 2}
        try:
            respons_page = requests.get('https://cars.av.by/filter?', params=params, headers={'user-agent': f'{self.user}'})
        except ConnectionError:
            return 0

        if respons_page.status_code == 200:
            data_soup = bs(respons_page.text, 'lxml')
            cout_ad = self.get_car_dict(data_soup, param = 1)[0]
            if cout_ad == 0:
                return 0
            
        self.count_page = math.ceil(cout_ad / 25)

        if self.count_page > 1 and self.brand_id != 0 and self.model_id != 0:
            for page in range(2, self.count_page + 1):
                params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'brands[0][generation]': self.generations_id, 'condition[0]': 2, 'page': page, 'sort': 2}
                try:
                    respons_page = requests.get('https://cars.av.by/filter?', params=params, headers={'user-agent': f'{self.user}'})
                except ConnectionError:
                    return 0
                
                if respons_page.status_code == 200:
                    data_soup = bs(respons_page.text, 'lxml')
                    self.get_car_dict(data_soup)
                else:
                    return 0

    def __call__(self): # -> self.car, self.count_page
        page = self.get_page()
        if page == 0:
            return 0, 0
        else:
            return self.car, self.count_page
    
class Search_cars(): # -> deviated_car_list
    def __init__(self, car_list:list=[], count_page:int=0, deviation_procent:int=60):  
        self.car_list = car_list
        self.count_page = count_page
        self.deviation_procent = deviation_procent
        self.deviation_price = 0
        self.deviated_car_list = []
        self.arg_price = 0

    def get_average_market_value(self):
        self.count_items, total_price = 0, 0
        for i in range(self.count_page):
            for item in self.car_list[i]:
                self.count_items += 1
                total_price += item['price']
                
        self.arg_price = (total_price/self.count_items)
        self.deviation_price = self.arg_price - ((self.arg_price * self.deviation_procent) / 100)
    
    def serch_deviated_car_list(self):
        for i in range(self.count_page):
            for item in self.car_list[i]:
                if item['price'] <= self.deviation_price:
                    self.deviated_car_list.append(item)
                    
    def __call__(self):
        self.get_average_market_value()
        self.serch_deviated_car_list()
        return self.deviated_car_list, self.arg_price
    

#######################################
def get_region():
    '''
    Возвращает список областей
    # бот выводит назвнаия областей и отдаёт 'id' 
    '''
    region = []
    for region_dikt in REGION:
        region.append({region_dikt['region_name']:region_dikt['id']})
    return region

def get_city_for_region(region_id):
    '''Возвращает список городов в конкретной области по id области'''
    city = []
    for city_dikt in REGION[region_id]['city']:
        city.append({city_dikt['city_name']:city_dikt['id']})
    return city
#######################################