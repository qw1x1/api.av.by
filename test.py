import requests
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
import lxml
import json
import math


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

file = 'page.htm'

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
def get_car_dict( page, param):
    car_list = []
    respons_list = []
    with open(page, 'r', encoding="utf-8") as htm:
        data_soup = bs(htm, 'lxml')
        if param == 1:
            count_ad = int("".join(count for count in data_soup.find(class_="listing__container").find(class_='listing__header').find(class_='listing__title').text if  count.isdecimal()))
            respons_list = [count_ad]
        for result in data_soup.find(class_="listing__items").find_all('div', class_="listing-item__wrap"):
            name_car = result.find('div', class_="listing-item__about").text
            link_car = 'https://cars.av.by' + result.find('div', class_="listing-item__about").find('a', class_="listing-item__link").get('href')
            params_to_car = result.find(class_="listing-item__params").text
            car_mileage = result.find('div', class_="listing-item__params").find('span').text
            price_car = int("".join(price for price in result.find(class_="listing-item__prices").find(class_="listing-item__priceusd").text if  price.isdecimal()))
            # if result.find(class_="listing-item__message"):
            description_car = 0 #result.find(class_="listing-item__message").text[:150]
            location = result.find(class_="listing-item__info").find(class_="listing-item__location").text

            car_list.append({'name':name_car, 'lank':link_car, 'parametrs': params_to_car, 'mileage': car_mileage, 'price': price_car, 'description': description_car, 'location': location})
        
        with open('car.json', 'a', encoding="utf-8") as s_file:
            json.dump(car_list, s_file, indent=4, ensure_ascii=False)
    return  respons_list

# count = get_car_dict('page.htm', param = 0)

# if bool(count) is True:
#     print(count[0])



def get_page(): # -> 1 page
    params = {'brands[0][brand]': 6, 'brands[0][model]': 10, 'year[min]': 1890, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 30000, 'condition[0]': 2, 'sort': 2}
    respons_page = requests.get('https://cars.av.by/filter?', params=params)
    if respons_page.status_code == 200:
        with open('page.htm', 'w', encoding="utf-8") as htm:
            htm.write(respons_page.text)
            cout_ad = get_car_dict('page.htm', param = 1)[0]
    # После запроса записываем ответ в файл т.к respons_page перезапишиться на некст итерации если она будет и распарсиваем его 
    # После первого запроса нужно распарсить страницу и достать количестро объявлений и разделить на 25 с округлением в большую сторону полусим число страниц / cout_ad - кол-во объявлений
    count_page = math.ceil( cout_ad / 25)
    if count_page > 1:
        for page in range(2, count_page + 2):
            params = {'brands[0][brand]': 6, 'brands[0][model]': 10, 'year[min]': 1980, 'year[max]': 2023, 'price_usd[min]': 100, 'price_usd[max]': 30000, 'condition[0]': 2, 'page': page, 'sort': 2}
            respons_page = requests.get('https://cars.av.by/filter?', params=params)
            if respons_page.status_code == 200:
                with open('page.htm', 'w', encoding="utf-8") as htm:
                    htm.write(respons_page.text)
                    cout_ad = get_car_dict('page.htm', param = 0)
            # После запроса записываем ответ в файл т.к respons_page перезапишиться на некст итерации и распарсиваем его 
    return page

get_page()