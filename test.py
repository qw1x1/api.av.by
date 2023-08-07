import requests 
import json

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



