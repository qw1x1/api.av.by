import requests
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
import json
import math

brand = {
    "Abarth": 10297,
    "Acura": 1444,
    "Alfa Romeo": 1,
    "Alpina": 5940,
    "ARO": 5324,
    "Asia": 5772,
    "Aston Martin": 2325,
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
    "Lamborghini": 2437,
    "Lancia": 572,
    "Land Rover": 584,
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

class Select_car: # -> brand_id, model_id

    def __init__(self, brand) -> None:
        self.brand_id = 0
        self.model_id = 0
        self.brand = brand
        self.model = {}
        self.user = User().random 

    # Пока в консоль :)
    @staticmethod
    def output_car(data): # -> id
        for key, value in data.items():
            print(key, value)
        print()
        key = str(input())
        return data[key]

    def get_data_select_car(self, params, data):
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/' + params, headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_data = json.loads(respons_list.text)
            for i in range(len(respons_data)):
                self.model[respons_data[i]['name']] = respons_data[i]['id']
                
    def __call__(self): # -> brand_id, model_id
        self.brand_id = self.output_car(self.brand)
        self.get_data_select_car(str(self.brand_id) +'/models', self.model)
        self.model_id = self.output_car(self.model)
        return self.brand_id, self.model_id
    
class Pars_info_id_file():
    
    def __init__(self, year_min=1910, year_max = 2023, price_min = 0, price_max = 0, *args) -> None:
        self.year_min = year_min
        self.year_max = year_max
        self.price_min = price_min
        self.price_max = price_max
        self.brand_id, self.model_id = args[0], args[1]

    def get_page(self): # -> 1 page
        params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'year[min]': self.year_min, 'year[max]': self.year_max, 'price_usd[min]': self.price_min, 'price_usd[max]': self.price_max, 'condition[0]': 2, 'sort': 2}
        respons_page = requests.get('https://cars.av.by/filter?', params=params)
        data_soup = bs(respons_page, 'lxml')
        self.count_page = data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text
        # После запроса записываем ответ в файл т.к respons_page перезапишиться на некст итерации если она будет и распарсиваем его 
        # После первого запроса нужно распарсить страницу и достать количестро объявлений и разделить на 25 с округлением в большую сторону полусим число страниц / cout_ad - кол-во объявлений
        self.count_page = math.ceil( cout_ad / 25)
        if self.count_page > 1:
            for page in range(2, self.count_page + 2):
                params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'year[min]': self.year_min, 'year[max]': self.year_max, 'price_usd[min]': self.price_min, 'price_usd[max]': self.price_max, 'condition[0]': 2, 'page': page, 'sort': 2}
                respons_page = requests.get('https://cars.av.by/filter?', params=params)
                # После запроса записываем ответ в файл т.к respons_page перезапишиться на некст итерации и распарсиваем его 
        return page
    
    def pars_renspons_page_data(self, respons_page):
        pass


def main():
    obj = Select_car(brand)
    car_crit = obj()
    print(car_crit[0], car_crit[1])


if __name__ == "__main__":
	main()