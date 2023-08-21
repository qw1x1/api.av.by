import requests, json, math
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs

brand = {
    "Acura": 1444,
    "Alfa Romeo": 1,
    "Audi": 6,
    "BMW": 8,
    "Buick": 1506,
    "BYD": 5459,
    "Cadillac": 40,
    "Changan": 2632,
    "Chery": 1998,
    "Chevrolet": 41,
    "Chrysler": 42,
    "Citroen": 43,
    "Cupra": 10236,
    "Dacia": 1841,
    "Daewoo": 46,
    "Daihatsu": 47,
    "Dodge": 45,
    "Dongfeng": 5780,
    "Dongfeng Honda": 10106,
    "FAW": 2465,
    "Fiat": 301,
    "Ford": 330,
    "Geely": 2012,
    "Genesis": 10006,
    "GMC": 372,
    "Great Wall": 1726,
    "Haval": 5782,
    "Honda": 383,
    "Hyundai": 433,
    "Infiniti": 1343,
    "Jaguar": 526,
    "Jeep": 540,
    "Kia": 545,
    "Lada (ВАЗ)": 1279,
    "Lancia": 572,
    "Land Rover": 584,
    "Lexus": 589,
    "Lifan": 2586,
    "Lincoln": 601,
    "LiXiang": 10209,
    "Maserati": 1625,
    "Mazda": 634,
    "Mercedes-Benz": 683,
    "Mitsubishi": 834,
    "Nissan": 892,
    "Opel": 966,
    "Peugeot": 989,
    "Porsche": 1485,
    "Renault": 1039,
    "Rover": 1067,
    "Saab": 1085,
    "SEAT": 1091,
    "Skoda": 1126,
    "SsangYong": 1597,
    "Subaru": 1136,
    "Suzuki": 1155,
    "Tesla": 2521,
    "Toyota": 1181,
    "Volkswagen": 1216,
    "Volvo": 1238,
}

class Get_model():
    def __init__(self):
        self.user = User().random 
        self.model_dict = {}

    def get_data_select_car(self, params):
        self.model_dict.clear()
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/' + params, headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_data = json.loads(respons_list.text)
            for i in range(len(respons_data)):
                self.model_dict[respons_data[i]['name']] = respons_data[i]['id']
        return self.model_dict
    
class Pars_info_id_file(): # -> car_list
    def __init__(self, year_min=1910, year_max=2023, price_min=0, price_max=0, brand_id=0, model_id=0):
        self.year_min = year_min
        self.year_max = year_max
        self.price_min = price_min
        self.price_max = price_max
        self.brand_id, self.model_id = brand_id, model_id
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
            name_car = result.find('div', class_="listing-item__about").text
            link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            params_to_car = result.find(class_="listing-item__params").text
            car_mileage = result.find('div', class_="listing-item__params").find('span').text
            price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            description_car = 'Без описания'
            if result.find(class_="listing-item__message"):
                description_car = result.find(class_="listing-item__message").text[:150]
            location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

            car_list.append({'name':name_car, 'lank':link_car, 'parametrs': params_to_car, 'mileage': car_mileage, 'price': price_car, 'description': description_car, 'location': location})
        self.car.append(car_list)
        return  respons_list

    def get_page(self): # -> Return 1 page 
        params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'year[min]': self.year_min, 'year[max]': self.year_max, 'price_usd[min]': self.price_min, 'price_usd[max]': self.price_max, 'condition[0]': 2, 'sort': 2}
        respons_page = requests.get('https://cars.av.by/filter?', params=params, headers={'user-agent': f'{self.user}'})
        if respons_page.status_code == 200:
            data_soup = bs(respons_page.text, 'lxml')
            cout_ad = self.get_car_dict(data_soup, param = 1)[0]
            if cout_ad == 0:
                return 0
            
        
        self.count_page = math.ceil(cout_ad / 25)
        if self.count_page > 1:
            for page in range(2, self.count_page + 1):
                params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'year[min]': self.year_min, 'year[max]': self.year_max, 'price_usd[min]': self.price_min, 'price_usd[max]': self.price_max, 'condition[0]': 2, 'page': page, 'sort': 2}
                respons_page = requests.get('https://cars.av.by/filter?', params=params, headers={'user-agent': f'{self.user}'})
                if respons_page.status_code == 200:
                    data_soup = bs(respons_page.text, 'lxml')
                    self.get_car_dict(data_soup)

    def __call__(self): # -> self.car, self.count_page
        page = self.get_page()
        if page == 0:
            return 0
        else:
            page
            return self.car, self.count_page
    
class Search_cars(): # -> deviated_car_list
    def __init__(self, car_list:list=[], count_page:int=0, deviation_procent:int=55):  
        self.car_list = car_list
        self.count_page = count_page
        self.deviation_procent = deviation_procent
        self.deviation_price = 0
        self.deviated_car_list = []

    def get_average_market_value(self):
        count_items, total_price = 0, 0
        for i in range(self.count_page):
            for item in self.car_list[i]:
                count_items += 1
                total_price += item['price']
                
        arg_price = (total_price/count_items)
        self.deviation_price = arg_price - ((arg_price * self.deviation_procent) / 100)
    
    def serch_deviated_car_list(self):
        for i in range(self.count_page):
            for item in self.car_list[i]:
                if item['price'] <= self.deviation_price:
                    self.deviated_car_list.append(item)

    def __call__(self):
        self.get_average_market_value()
        self.serch_deviated_car_list()
        return self.deviated_car_list
