import requests, json, math, time, datetime
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
from api.controls import set_time_sub, get_time_sub # BOT
# from controls import set_time_sub, get_time_sub # debug

MONTH_IN_SECONDS = 2592000

CITY_IN_REGION = [
{'id': 0, 'region_name': 'Брестская обл.', 'city':[
    {'city_name': 'Брест', 'id': 8},
    {'city_name': 'Барановичи', 'id': 116},
    {'city_name': 'Белоозёрск', 'id': 796},
    {'city_name': 'Береза', 'id': 117},
    {'city_name': 'Высокое', 'id': 797},
    {'city_name': 'Ганцевичи', 'id': 118},
    {'city_name': 'Давид-Городок', 'id': 790},
    {'city_name': 'Дрогичин', 'id': 119},
    {'city_name': 'Жабинка', 'id': 120},
    {'city_name': 'Иваново', 'id': 121}, 
    {'city_name': 'Ивацевичи', 'id': 122},
    {'city_name': 'Каменец', 'id': 123},
    {'city_name': 'Кобрин', 'id': 124}, 
    {'city_name': 'Коссово', 'id': 798},
    {'city_name': 'Лунинец', 'id': 125},
    {'city_name': 'Ляховичи', 'id': 126},
    {'city_name': 'Малорита', 'id': 127},
    {'city_name': 'Микашевичи', 'id': 789},
    {'city_name': 'Пинск', 'id': 128}, 
    {'city_name': 'Пружаны', 'id': 129}, 
    {'city_name': 'Столин', 'id': 130}]},
{'id': 1, 'region_name': 'Витебская обл.', 'city':[
    {'city_name': 'Витебск', 'id': 7},
    {'city_name': 'Барань', 'id': 792},
    {'city_name': 'Бешенковичи', 'id': 131}, 
    {'city_name': 'Браслав', 'id': 132},
    {'city_name': 'Верхнедвинск', 'id': 133},
    {'city_name': 'Глубокое', 'id': 134}, 
    {'city_name': 'Городок', 'id': 135},
    {'city_name': 'Дисна', 'id': 793}, 
    {'city_name': 'Докшицы', 'id': 136},
    {'city_name': 'Дубровно', 'id': 137},
    {'city_name': 'Лепель', 'id': 138},
    {'city_name': 'Лиозно', 'id': 139}, 
    {'city_name': 'Миоры', 'id': 140},
    {'city_name': 'Новолукомль', 'id': 791},
    {'city_name': 'Новополоцк', 'id': 141},
    {'city_name': 'Орша', 'id': 142},
    {'city_name': 'Полоцк', 'id': 143},
    {'city_name': 'Поставы', 'id': 144},
    {'city_name': 'Россоны', 'id': 145},
    {'city_name': 'Сенно', 'id': 146},
    {'city_name': 'Толочин', 'id': 147},
    {'city_name': 'Ушачи', 'id': 148},
    {'city_name': 'Чашники', 'id': 149}, 
    {'city_name': 'Шарковщина', 'id': 150},
    {'city_name': 'Шумилино', 'id': 151}]},
{'id': 2, 'region_name': 'Гомельская обл.', 'city':[
    {'city_name': 'Гомель', 'id': 9},
    {'city_name': 'Брагин', 'id': 152},
    {'city_name': 'Буда-Кошелево', 'id': 153},
    {'city_name': 'Василевичи', 'id': 794},
    {'city_name': 'Ветка', 'id': 154},
    {'city_name': 'Добруш', 'id': 155},
    {'city_name': 'Ельск', 'id': 156},
    {'city_name': 'Житковичи', 'id': 157},
    {'city_name': 'Жлобин', 'id': 158},
    {'city_name': 'Калинковичи', 'id': 159},
    {'city_name': 'Корма', 'id': 161},
    {'city_name': 'Лельчицы', 'id': 162},
    {'city_name': 'Лоев', 'id': 163}, 
    {'city_name': 'Мозырь', 'id': 164}, 
    {'city_name': 'Наровля', 'id': 165},
    {'city_name': 'Октябрьский', 'id': 166},
    {'city_name': 'Петриков', 'id': 167},
    {'city_name': 'Речица', 'id': 168}, 
    {'city_name': 'Рогачев', 'id': 169},
    {'city_name': 'Светлогорск', 'id': 170},
    {'city_name': 'Сосновый Бор', 'id': 803}, 
    {'city_name': 'Туров', 'id': 795},
    {'city_name': 'Хойники', 'id': 172},
    {'city_name': 'Чечерск', 'id': 171}]}, 
{'id': 3, 'region_name': 'Гродненская обл.', 'city':[
    {'city_name': 'Гродно', 'id': 3},
    {'city_name': 'Берёзовка', 'id': 800},
    {'city_name': 'Большая Берестовица', 'id': 173},
    {'city_name': 'Волковыск', 'id': 174}, 
    {'city_name': 'Вороново', 'id': 175},
    {'city_name': 'Дятлово', 'id': 176},
    {'city_name': 'Зельва', 'id': 177},
    {'city_name': 'Ивье', 'id': 178},
    {'city_name': 'Кореличи', 'id': 179},
    {'city_name': 'Лида', 'id': 180},
    {'city_name': 'Мосты', 'id': 181}, 
    {'city_name': 'Новогрудок', 'id': 182}, 
    {'city_name': 'Островец', 'id': 183}, 
    {'city_name': 'Ошмяны', 'id': 184},
    {'city_name': 'Свислочь', 'id': 185}, 
    {'city_name': 'Скидель', 'id': 799},
    {'city_name': 'Слоним', 'id': 186}, 
    {'city_name': 'Сморгонь', 'id': 187},
    {'city_name': 'Щучин', 'id': 188},
    {'city_name': 'Россь', 'id': 806}]},
{'id': 4, 'region_name': 'Минская обл.', 'city':[
    {'city_name': 'Минск', 'id': 2}, 
    {'city_name': 'Березино', 'id': 92},
    {'city_name': 'Борисов', 'id': 93},
    {'city_name': 'Вилейка', 'id': 94},
    {'city_name': 'Воложин', 'id': 95},
    {'city_name': 'Дзержинск', 'id': 96},
    {'city_name': 'Жодино', 'id': 97}, 
    {'city_name': 'Заславль', 'id': 98},
    {'city_name': 'Клецк', 'id': 99},
    {'city_name': 'Копыль', 'id': 100},
    {'city_name': 'Крупки', 'id': 101},
    {'city_name': 'Логойск', 'id': 102},
    {'city_name': 'Любань', 'id': 103},
    {'city_name': 'Марьина Горка', 'id': 104},
    {'city_name': 'Михановичи', 'id': 804},
    {'city_name': 'Молодечно', 'id': 105},
    {'city_name': 'Мядель', 'id': 106},
    {'city_name': 'Несвиж', 'id': 107},
    {'city_name': 'Прилуки', 'id': 805},
    {'city_name': 'Пуховичи', 'id': 108},
    {'city_name': 'Раков', 'id': 788},
    {'city_name': 'Руденск', 'id': 248},
    {'city_name': 'Слуцк', 'id': 109},
    {'city_name': 'Смолевичи', 'id': 110},
    {'city_name': 'Солигорск', 'id': 111},
    {'city_name': 'Старые Дороги', 'id': 112},
    {'city_name': 'Столбцы', 'id': 113},
    {'city_name': 'Узда', 'id': 114},
    {'city_name': 'Фаниполь', 'id': 160},
    {'city_name': 'Червень', 'id': 115}]}, 
{'id': 5, 'region_name': 'Могилевская обл.', 'city':[
    {'city_name': 'Могилев', 'id': 6},
    {'city_name': 'Белыничи', 'id': 189},
    {'city_name': 'Бобруйск', 'id': 190},
    {'city_name': 'Быхов', 'id': 191},
    {'city_name': 'Глуск', 'id': 192},
    {'city_name': 'Горки', 'id': 193},
    {'city_name': 'Дрибин', 'id': 194},
    {'city_name': 'Кировск', 'id': 195},
    {'city_name': 'Климовичи', 'id': 196},
    {'city_name': 'Кличев', 'id': 197},
    {'city_name': 'Костюковичи', 'id': 198},
    {'city_name': 'Краснополье', 'id': 199}, 
    {'city_name': 'Кричев', 'id': 200}, 
    {'city_name': 'Круглое', 'id': 201},
    {'city_name': 'Мстиславль', 'id': 202},
    {'city_name': 'Осиповичи', 'id': 203},
    {'city_name': 'Славгород', 'id': 204},
    {'city_name': 'Хотимск', 'id': 205},
    {'city_name': 'Чаусы', 'id': 206}, 
    {'city_name': 'Чериков', 'id': 207},
    {'city_name': 'Шклов', 'id': 208}]}
]

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
                count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if count.isdecimal()))
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

##################REGION#####################
def get_region():
    '''
    Возвращает список областей
    # бот выводит назвнаия областей и отдаёт 'id' 
    '''
    region = []
    for region_dikt in CITY_IN_REGION:
        region.append({region_dikt['region_name']:region_dikt['id']})
    return region

def get_city_for_region(region_id):
    '''Возвращает список городов в конкретной области по id области'''
    city = []
    for city_dikt in CITY_IN_REGION[region_id]['city']:
        city.append({city_dikt['city_name']:city_dikt['id']})
    return city
################END_REGION###################

####################SUB######################
def set_time(telegram_id=0):
    """
    Записывает время подписки пользователю и отправляет True в ответ
    """
    time_sub = int(time.time()) + MONTH_IN_SECONDS
    set_time_sub(telegram_id=telegram_id, time=time_sub)
    return True

def get_sub_time(telegram_id=0):
    """
    Вернет остаток времени подписки в формате дни.часы.минуты.секунды, если подписки нет то вернет False
    """
    time_sub_user = get_time_sub(telegram_id=telegram_id)
    time_now = int(time.time())
    middle_time = int(time_sub_user) - time_now

    if middle_time <= 0:
        return False
        # При этом отвкте вывксит пользователю f'Время Вашей подписки имтекло' и предложение покупки подписки
    else:
        time_sud = str(datetime.timedelta(seconds=middle_time))
        time_sud = time_sud.replace('days', 'дней').replace('day', 'день')
        return time_sud
##################END_SUB####################
    
# set_time(telegram_id=633279160)
# print(get_sub_time(telegram_id=633279160))