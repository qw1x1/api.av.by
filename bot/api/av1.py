import requests, json, math
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs

brand = {
    "Abarth": 10297,
    "Acura": 1444,
    "Alfa Romeo": 1,
    "Alfa": 1,
    "Alpina": 5940,
    "ARO": 5324,
    "Asia": 5772,
    "Aston Martin": 2325,
    "Aston": 2325,
    "Audi": 6,
    "Avatr": 10346,
    "BAIC ": 10034,
    "Baojun": 10337,
    "Bentley": 1676,
    "BMW": 8,
    "Brilliance": 2210,
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
    "Datsun": 2578,
    "Denza": 10287,
    "Derways": 5109,
    "Dodge": 45,
    "Dongfeng": 5780,
    "Dongfeng Honda": 10106,
    "Eagle": 10240,
    "Everus": 10224,
    "EXEED": 10303,
    "FAW": 2465,
    "Ferrari": 288,
    "Fiat": 301,
    "Fisker": 2323,
    "Ford": 330,
    "Foton": 2355,
    "FSO": 5526,
    "GAC": 10131,
    "GAC Honda": 10222,
    "Geely": 2012,
    "Genesis": 10006,
    "GMC": 372,
    "Gonow": 6005,
    "Great Wall": 1726,
    "Great": 1726,
    "Hafei": 2215,
    "Haima": 5070,
    "Haval": 5782,
    "HiPhi": 10279,
    "Honda": 383,
    "Hongqi": 10275,
    "Hongxing": 2681,
    "Hozon": 10259,
    "Hummer": 1498,
    "Hycan": 10326,
    "Hyundai": 433,
    "Infiniti": 1343,
    "Iran Khodro": 2022,
    "Iran": 2022,
    "Isuzu": 461,
    "JAC": 2030,
    "Jaguar": 526,
    "Jeep": 540,
    "Jetour": 10362,
    "Jiangling": 2272,
    "Joylong": 10188,
    "Kandi": 10238,
    "Kia": 545,
    "Lada (ВАЗ)": 1279,
    "Lada": 1279,
    "Lamborghini": 2437,
    "Lancia": 572,
    "Land Rover": 584,
    "Land": 584,
    "Leapmotor": 10268,
    "Lexus": 589,
    "Lifan": 2586,
    "Lincoln": 601,
    "LiXiang": 10209,
    "Lotus": 2295,
    "Mahindra": 5957,
    "Maserati": 1625,
    "Maybach": 2169,
    "Mazda": 634,
    "McLaren": 5970,
    "Mercedes-Benz": 683,
    "Mercury": 825,
    "MG": 1906,
    "Microcar": 10090,
    "MINI": 1850,
    "Mitsubishi": 834,
    "Morgan": 5937,
    "Nissan": 892,
    "Oldsmobile": 1364,
    "Opel": 966,
    "Peugeot": 989,
    "Piaggio": 2221,
    "Plymouth": 1012,
    "Polestar": 10042,
    "Pontiac": 1022,
    "Porsche": 1485,
    "Proton": 1609,
    "RAM": 10226,
    "Ravon": 5503,
    "Renault": 1039,
    "Renault Samsung": 10100,
    "Roewe": 5800,
    "Rolls-Royce": 5100,
    "Rover": 1067,
    "Saab": 1085,
    "Saipa": 5029,
    "Santana": 5517,
    "Saturn": 1703,
    "Scion": 2698,
    "SEAT": 1091,
    "Seres": 10289,
    "Shanghai Maple": 5822,
    "Shanghai": 5822,
    "Skoda": 1126,
    "Skywell": 10308,
    "Smart": 2449,
    "SRM": 10350,
    "SsangYong": 1597,
    "Subaru": 1136,
    "Suzuki": 1155,
    "Tata": 5447,
    "Tatra": 10161,
    "Tesla": 2521,
    "Think": 10013,
    "Tianma": 5520,
    "Toyota": 1181,
    "Trabant": 5080,
    "VGV": 10368,
    "Volkswagen": 1216,
    "Volvo": 1238,
    "Vortex": 5437,
    "Voyah": 10244,
    "Wartburg": 1857,
    "Weltmeister": 10067,
    "Wuling": 10334,
    "Xpeng": 6019,
    "Yudo": 10285,
    "Zeekr": 10185,
    "Zotye": 2510,
    "ZX": 5066,
    "Богдан": 5076,
    "ГАЗ": 1310,
    "ЕрАЗ": 10094,
    "ЗАЗ": 1551,
    "ИЖ": 2894,
    "ЛуАЗ": 2345,
    "Москвич": 2051,
    "РАФ": 5252,
    "ТагАЗ": 5032,
    "УАЗ": 1464,
    "Эксклюзив": 5019
}
revers_brand = {
    1444: 'Acura',
    1: 'Alfa Romeo',
    6: 'Audi',
    8: 'BMW',
    1506: 'Buick',
    5459: 'BYD',
    40: 'Cadillac',
    2632: 'Changan',
    1998: 'Chery',
    41: 'Chevrolet',
    42: 'Chrysler',
    43: 'Citroen',
    10236: 'Cupra',
    1841: 'Dacia',
    46: 'Daewoo',
    47: 'Daihatsu',
    45: "Dodge",
    5780: "Dongfeng",
    10106: "Dongfeng Honda",
    2465: "FAW",
    301: "Fiat",
    330: "Ford",
    2012: "Geely",
    10006: "Genesis",
    372: "GMC",
    1726: "Great Wall",
    5782: "Haval",
    383: "Honda",
    433: "Hyundai",
    1343: "Infiniti",
    526: "Jaguar",
    540: "Jeep",
    545: "Kia",
    1279: "Lada (ВАЗ)",
    572: "Lancia",
    584: "Land Rover",
    589: "Lexus",
    2586: "Lifan",
    601: "Lincoln",
    10209: "LiXiang",
    1625: "Maserati",
    634: "Mazda",
    683: "Mercedes-Benz",
    834: "Mitsubishi",
    892: "Nissan",
    966: "Opel",
    989: "Peugeot",
    1485: "Porsche",
    1039: "Renault",
    1067: "Rover",
    1085: "Saab",
    1091: "SEAT",
    1126: "Skoda",
    1597: "SsangYong",
    1136: "Subaru",
    1155: "Suzuki",
    2521: "Tesla",
    1181: "Toyota",
    1216: "Volkswagen",
    1238: "Volvo",
}

class Get_model_or_generations():
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
            return 0
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
    

# dict_to_car = Pars_info_id_file(brand_id=634, model_id=640, generations_id=1350)
# params = dict_to_car()
# print(params[0], params[1])