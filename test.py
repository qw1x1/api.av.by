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

with open('brand.json', 'r') as brand:
    data_brand = json.load(brand)
    for i in range(len(data_brand)):
        print(data_brand[i]['id'], data_brand[i]['name'])
    id = int(input())
    print(data_brand[id])


