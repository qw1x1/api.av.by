from typing import Any
import requests
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
import lxml
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
# car_dict = {}

# # Находит обьявление и если оно активно, то добавляет в car_dict.
# def get_car_by_id(id):
#     data = requests.get('https://api.av.by/offers/' + str(id))
#     car_obj = json.loads(data.text)
#     if 'publicUrl' in car_obj and car_obj['publicStatus']['name'] == 'active':
#         return car_obj
#     else:
#         return 'NANE'
    
# # Перебераем id и кидаем в get_car_by_id
# for id in range(100757688 , 100757699):
#     if get_car_by_id(id) != 'NANE':
#         # print(get_car_by_id(id)['properties']) locationName
#         car_dict[str(id)] = get_car_by_id(id)['properties'][0]['value'], get_car_by_id(id)['publicUrl'], get_car_by_id(id)['properties'][0]['value'], get_car_by_id(id)['properties'][1]['value'],get_car_by_id(id)['properties'][2]['value'], get_car_by_id(id)['properties'][3]['value'], get_car_by_id(id)['properties'][-1]['value'], get_car_by_id(id)['properties'][-3]['value'],get_car_by_id(id)['properties'][6]['value'], get_car_by_id(id)['properties'][4]['value'], get_car_by_id(id)['properties'][5]['value'], get_car_by_id(id)['locationName']

# # Записываем в файл все активные обьявления
# with open('car.json', 'w') as car:
#     json.dump(car_dict, car)


# # with open('car.json') as json_file:
# #    data = (json.load(json_file))
# # for id in data:  
# #     print(data[id][1], data[id][2], data[id][3], data[id][4], data[id][5])
# #     print('Цена:', data[id][6])  
# #     print('Пробег:', data[id][7]) 
# #     print('Ходовая:', data[id][8], data[id][9], data[id][10]) 
# #     print('Местоположение:', data[id][11])
# #     print()

# try:
#     brand = byUsrUrlObj.read()
#     qUserData = json.loads(brand).decode('utf-8')
#     questionSubjs = qUserData["all"]["questions"]
# except ValueError:  # jrrrrrrrrr
    # print('Decoding JSON has failed')
# with open('brand.json', encoding="utf-8") as json_file:
#    data = (json.load(json_file))

########################################################################################################################################

# def get_model_car_list():
#     respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models', headers={'user-agent': f'{self.user}'})
#     respons_model = json.loads(respons_list.text)
#     with open('model.json', 'w', encoding="utf-8") as model:
#         json.dump(respons_model, model, indent=4, ensure_ascii=False)

# def get_model_car_list():
#         brand_id = 683
#         data_model={}
#         respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models')
#         respons_model = json.loads(respons_list.text)

#         for i in range(len(respons_model)):
#             data_model[respons_model[i]['id']] = respons_model[i]['name']
#             with open('model.json', 'w', encoding="utf-8") as model:
#                 json.dump(data_model, model, indent=4, ensure_ascii=False)

# def get_generations_car_list():
#     data_generations={}
#     brand_id, model_id = 683, 5879
#     respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models/'+ str(model_id) +'/generations')
#     respons_generations = json.loads(respons_list.text)
#     for i in range(len(respons_generations)):
#         data_generations[respons_generations[i]['id']] = respons_generations[i]['name']
#         with open('generations.json', 'w', encoding="utf-8") as generations:
#             json.dump(data_generations, generations, indent=4, ensure_ascii=False)
# get_generations_car_list()

    # print(data_brand.setdefault(key, 0000000000))

# Последовательно получаем выбераемые данные от пользователя, если пользователь ни чего не выбрал передать null или nane
# def select_item(self):
#     brand_id = self.get_brand_car_list()
#     model_id = self.get_model_car_list(brand_id)
#     generations_id = self.get_generations_car_list(brand_id, model_id)
#     return brand_id , model_id, generations_id


# Выполняем поиск данных с сервера изходя из полученных данных от пользователя
# def get_page_car(*args):
#     if len(args) == 0:
#         params = {'condition[0]': 2, 'sort': 2}
#     elif len(args) == 1:
#         params = {'brands[0][brand]': args[0], 'condition[0]': 2, 'sort': 2}
#     elif len(args) == 2:
#         params = {'brands[0][brand]': args[0], 'brands[0][model]': args[1], 'condition[0]': 2, 'sort': 2}
#     elif len(args) == 3:
#         params = {'brands[0][brand]': args[0], 'brands[0][model]': args[1], 'brands[0][generation]': args[2], 'condition[0]': 2, 'sort': 2}
#     page_htm = requests.get('https://cars.av.by/filter?', params=params)
#     # Если страница получина, записываем данные в файл (нужно дороботать сбор со всех имеющихся страниц) + распасить и подготовить данные для оброботки
#     if page_htm.status_code == 200:
#         with open('page.htm', 'w', encoding="utf-8") as htm:
#             data = htm.write(page_htm.text)


# def get_brand_car_list():
#         brand_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items')
#         data_brand = json.loads(brand_list.text)
#         with open('brand.json', 'w', encoding="utf-8") as brand:
#             json.dump(data_brand, brand, indent=4, ensure_ascii=False)

# get_brand_car_list()



# with open(r, 'r', encoding="utf-8") as brand:
#     data_brand = json.load(brand)
#     for key, value in data_brand.items():
#         print(key, value)
#     key = str(input())
#     print()
#     print(data_brand[key])

# def output_car(file):
#     with open(file, 'r', encoding="utf-8") as file:
#         data = json.load(file)
#         for key, value in data.items():
#             print(key, value)
#         print()

#         key = str(input())
#         return data[key]
    
# r = 'brand.json'
# # print(output_car(r))


#         self.brand_id = 683
#         self.model_id = 5879
#         self.generations_id = 4508  or str('brand_id') +'/models/'+ str('model_id') +'/generations'


# def get_data_select_car(self, params):
#     data = {}
#     respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/' + params, headers={'user-agent': f'{self.user}'})
#     if respons_list.status_code == 200:
#         respons_data = json.loads(respons_list.text)
#         for i in range(len(respons_data)):
#             data[respons_data[i]['name']] = respons_data[i]['id'] 
#             with open('brand.json', 'w', encoding="utf-8") as file:
#                 json.dump(data, file, indent=4, ensure_ascii=False)



# params = str(683) +'/models'
# param = str(683) +'/models/'+ str(5879) +'/generations'
# get_brand_car_list(param)

# file = 'brand.json'



# params = {'brands[0][brand]': 6, 'brands[0][model]': 10,  'year[min]': 1970, 'year[max]': 2023, 'price_usd[min]': 0, 'price_usd[max]': 0, 'condition[0]': 2, 'page': 0, 'sort': 2}
# respons_page = requests.get('https://cars.av.by/filter?', params=params)
# print(respons_page.status_code)

# file = 'page.htm'

# with open(file, 'r', encoding="utf-8") as htm:
#     data_soup = bs(htm, 'lxml')
    
# count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))

# for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
#     name_car = result.find('div', class_="listing-item__about").text
#     link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
#     params_to_car = result.find(class_="listing-item__params").text
#     car_mileage = result.find('div', class_="listing-item__params").find('span').text
#     price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
#     if result.find(class_="listing-item__message"):
#         description_car = result.find(class_="listing-item__message").text[:150]
#     location = result.find(class_="listing-item__info").find(class_="listing-item__location").text
#     print(name_car, link_car, params_to_car, car_mileage, price_car, description_car, location, sep='\n')
#     print()
# print(count_ad)



# with open(file, 'a', encoding="utf-8") as s_file:
#      json.dump(car_list, s_file, indent=4, ensure_ascii=False)


# Принимет 1 страницу и генирирует словать с авто с полученой страницы
# param = 1, тогда нам отдаст количество страниц, иначе не отдаст 
# def get_car_dict(page, param = 0):
#     car_list = []
#     respons_list = []
#     with open(page, 'r', encoding="utf-8") as htm:
#         data_soup = bs(htm, 'lxml')
#         if param == 1:
#             count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))
#             respons_list = [count_ad]
#         for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
#             name_car = result.find('div', class_="listing-item__about").text
#             link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
#             params_to_car = result.find(class_="listing-item__params").text
#             car_mileage = result.find('div', class_="listing-item__params").find('span').text
#             price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
#             if result.find(class_="listing-item__message"):
#                 description_car = result.find(class_="listing-item__message").text[:150]
#             location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

#             car_list.append({'name':name_car, 'lank':link_car, 'parametrs': params_to_car, 'mileage': car_mileage, 'price': price_car, 'description': description_car, 'location': location})
        
#         with open('car.json', 'a', encoding="utf-8") as s_file:
#             json.dump(car_list, s_file, indent=4, ensure_ascii=False)
#     return  respons_list

# def get_page(): # -> 1 page
#     params = {'brands[0][brand]': 1, 'brands[0][model]': 3, 'year[min]': 1890, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 3000000, 'condition[0]': 2, 'sort': 2}
#     respons_page = requests.get('https://cars.av.by/filter?', params=params)
#     if respons_page.status_code == 200:
#         with open('page.htm', 'w', encoding="utf-8") as htm:
#             htm.write(respons_page.text)
#             cout_ad = get_car_dict('page.htm', param = 1)[0]
    
#     count_page = math.ceil( cout_ad / 25)
#     if count_page > 1:
#         for page in range(2, count_page + 1):
#             print(0)
#             params = {'brands[0][brand]': 1, 'brands[0][model]': 3, 'year[min]': 1980, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 3000000, 'condition[0]': 2, 'page': page, 'sort': 2}
#             respons_page = requests.get('https://cars.av.by/filter?', params=params)
#             if respons_page.status_code == 200:
#                 with open('page.htm', 'w', encoding="utf-8") as htm:
#                     htm.write(respons_page.text)
#                     cout_ad = get_car_dict('page.htm')

# get_page()









# car = []
# def get_car_dict(data_soup, param = 0):
#     car_list, respons_list = [], []
    
#     if param == 1:
#         count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))
#         respons_list = [count_ad]
#     for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
#         name_car = result.find('div', class_="listing-item__about").text
#         link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
#         params_to_car = result.find(class_="listing-item__params").text
#         car_mileage = result.find('div', class_="listing-item__params").find('span').text
#         price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
#         if result.find(class_="listing-item__message"):
#             description_car = result.find(class_="listing-item__message").text[:150]
#         location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

#         car_list.append({'name':name_car, 'lank':link_car, 'parametrs': params_to_car, 'mileage': car_mileage, 'price': price_car, 'description': description_car, 'location': location})


#     car.append(car_list)
#     print(len(car))


#     with open('car.json', 'a', encoding="utf-8") as s_file:
#         json.dump(car_list, s_file, indent=4, ensure_ascii=False)
#     return  respons_list

# def get_page(): # -> 1 page
#     params = {'brands[0][brand]': 6, 'brands[0][model]': 2278, 'year[min]': 1890, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 3000000, 'condition[0]': 2, 'sort': 2}
#     respons_page = requests.get('https://cars.av.by/filter?', params=params)
#     if respons_page.status_code == 200:
#         data_soup = bs(respons_page.text, 'lxml')
#         cout_ad = get_car_dict(data_soup, param = 1)[0]
    
#     count_page = math.ceil(cout_ad / 25)
#     if count_page > 1:
#         for page in range(2, count_page + 1):
#             params = {'brands[0][brand]': 6, 'brands[0][model]': 2278, 'year[min]': 1980, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 3000000, 'condition[0]': 2, 'page': page, 'sort': 2}
#             respons_page = requests.get('https://cars.av.by/filter?', params=params)
#             if respons_page.status_code == 200:
#                 data_soup = bs(respons_page.text, 'lxml')
#                 cout_ad = get_car_dict(data_soup)

# get_page()









# car = []
# def get_car_dict(data_soup, param = 0):
#     car_list, respons_list = [], []
    
#     if param == 1:
#         count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))
#         respons_list = [count_ad]
#     for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
#         name_car = result.find('div', class_="listing-item__about").text
#         link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
#         params_to_car = result.find(class_="listing-item__params").text
#         car_mileage = result.find('div', class_="listing-item__params").find('span').text
#         price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
#         if result.find(class_="listing-item__message"):
#             description_car = result.find(class_="listing-item__message").text[:150]
#         location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

#         car_list.append({'name':name_car, 'lank':link_car, 'parametrs': params_to_car, 'mileage': car_mileage, 'price': price_car, 'description': description_car, 'location': location})
#     car.append(car_list)
#     return  respons_list

# def get_page(): # -> 1 page
#     params = {'brands[0][brand]': 6, 'brands[0][model]': 2278, 'year[min]': 1890, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 3000000, 'condition[0]': 2, 'sort': 2}
#     respons_page = requests.get('https://cars.av.by/filter?', params=params)
#     if respons_page.status_code == 200:
#         data_soup = bs(respons_page.text, 'lxml')
#         cout_ad = get_car_dict(data_soup, param = 1)[0]
    
#     count_page = math.ceil(cout_ad / 25)
#     if count_page > 1:
#         for page in range(2, count_page + 1):
#             params = {'brands[0][brand]': 6, 'brands[0][model]': 2278, 'year[min]': 1980, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 3000000, 'condition[0]': 2, 'page': page, 'sort': 2}
#             respons_page = requests.get('https://cars.av.by/filter?', params=params)
#             if respons_page.status_code == 200:
#                 data_soup = bs(respons_page.text, 'lxml')
#                 cout_ad = get_car_dict(data_soup)

# get_page()




# class Pars_info_id_file(): # -> car_list
#     def __init__(self, year_min=1910, year_max = 2023, price_min = 0, price_max = 0, brand_id = 0, model_id = 0):
#         self.year_min = year_min
#         self.year_max = year_max
#         self.price_min = price_min
#         self.price_max = price_max
#         self.brand_id, self.model_id = brand_id, model_id
#         self.car = []

#     def get_car_dict(self, data_soup, param = 0): # -> Return list for car
#         car_list, respons_list = [], []
        
#         if param == 1:
#             count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))
#             respons_list = [count_ad]
#         for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
#             name_car = result.find('div', class_="listing-item__about").text
#             link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
#             params_to_car = result.find(class_="listing-item__params").text
#             car_mileage = result.find('div', class_="listing-item__params").find('span').text
#             price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
#             if result.find(class_="listing-item__message"):
#                 description_car = result.find(class_="listing-item__message").text[:150]
#             location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

#             car_list.append({'name':name_car, 'lank':link_car, 'parametrs': params_to_car, 'mileage': car_mileage, 'price': price_car, 'description': description_car, 'location': location})
#         self.car.append(car_list)
#         return  respons_list

#     def get_page(self): # -> Return 1 page 
#         params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'year[min]': self.year_min, 'year[max]': self.year_max, 'price_usd[min]': self.price_min, 'price_usd[max]': self.price_max, 'condition[0]': 2, 'sort': 2}
#         respons_page = requests.get('https://cars.av.by/filter?', params=params)
#         if respons_page.status_code == 200:
#             data_soup = bs(respons_page.text, 'lxml')
#             cout_ad = self.get_car_dict(data_soup, param = 1)[0]
        
#         self.count_page = math.ceil(cout_ad / 25)
#         if self.count_page > 1:
#             for page in range(2, self.count_page + 1):
#                 params = {'brands[0][brand]': self.brand_id, 'brands[0][model]': self.model_id, 'year[min]': self.year_min, 'year[max]': self.year_max, 'price_usd[min]': self.price_min, 'price_usd[max]': self.price_max, 'condition[0]': 2, 'page': page, 'sort': 2}
#                 respons_page = requests.get('https://cars.av.by/filter?', params=params)
#                 if respons_page.status_code == 200:
#                     data_soup = bs(respons_page.text, 'lxml')
#                     self.get_car_dict(data_soup)

#     def __call__(self): # -> self.car, self.count_page
#         self.get_page()
#         return self.car, self.count_page

# r = Pars_info_id_file(brand_id = 6, model_id = 2278)
# c = r()
# print(c[1])
# count_page = c[1]
# for i in range(count_page):
#     for item in c[0][i]:
#         print(item['price'])

# class Search_cars(): # -> deviated_car_list
#     def __init__(self, car_list:list=[], count_page:int=0, deviation_procent:int=0):  
#         self.car_list = car_list
#         self.count_page = count_page
#         self.deviation_procent = deviation_procent
#         self.deviation_price = 0
#         self.deviated_car_list = []

#     def get_average_market_value(self):
#         count_items, total_price = 0, 0
#         for i in range(self.count_page):
#             for item in self.car_list[i]:
#                 count_items += 1
#                 total_price += item['price']
#         arg_price = ((total_price/count_items) * self.deviation_procent) / 100
#         self.deviation_price = total_price - arg_price 
    
#     def serch_deviated_car_list(self):
#         for i in range(self.count_page):
#             for item in self.car_list[i]:
#                 if item['price'] <= self.deviation_price:
#                     self.deviated_car_list.append(item)

#     def __call__(self):
#         self.get_average_market_value()
#         self.serch_deviated_car_list()
#         return self.deviated_car_list





class Select_car: # -> brand_id, model_id
    def __init__(self, brand, metod_bran_id, metod_model_id) -> None:
        self.brand_id = 0
        self.model_id = 0
        self.brand = brand
        self.model = {}
        self.user = User().random
        self.metod_bran_id = metod_bran_id
        self.metod_model_id = metod_model_id

    def get_data_select_car(self, params):
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/' + params, headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_data = json.loads(respons_list.text)
            for i in range(len(respons_data)):
                self.model[respons_data[i]['name']] = respons_data[i]['id']

    def __call__(self): # -> brand_id, model_id
        self.brand_id = self.metod_bran_id(self.brand)
        self.get_data_select_car(str(self.brand_id) +'/models')
        self.model_id = self.metod_model_id(self.model)
        return self.brand_id, self.model_id
    



def metod_bran_id(data): 
    # Напишеш функцию для вывода и получения id, тип этой ток не в консоль а в тг_бот и предаш ее 2 параметрам классу Select_car(brand=brand, metod='''''ТУТ'''')
    for key, value in data.items():
        print(key, value)
    print()
    key = str(input())
    return data[key]

def metod_model_id(data): 
    # Напишеш функцию для вывода и получения id, тип этой ток не в консоль а в тг_бот и предаш ее 2 параметрам классу Select_car(brand=brand, metod='''''ТУТ'''')
    for key, value in data.items():
        print(key, value)
    print()
    key = str(input())
    return data[key]

obj = Select_car(brand=brand, metod_bran_id=metod_bran_id, metod_model_id=metod_model_id)
ger = obj()
print(ger)