import requests
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
import json

brand_id = 683 # mersedec-benz
model_id = 5879 # C-class
generations_id = 4508 # 202 - 1 generations

class Select_car: # Fills in files: brand, model, generations.

    def __init__(self) -> None:
        '''
            Вывод списков
            Получение последовательных ответов (ВАЖНО СОБЛЮДАТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ)

            API писать на REST?
        '''
        self.brand_id = 683
        self.model_id = 5879
        self.generations_id = 4508
        self.user = User().random # Инициализация объекта UserAgent в объекте Select_car
        self.brand = 'brand.json'
    @staticmethod
    def output_car(file):
        with open(file, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                print(key, value)
            print()

            key = str(input())
            return data[key]

    def get_brand_car_list(self): # этот метод можно удалить но оставть заполненный файл, т.к он неизменный(почти)
        data_brand={}
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items', headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_brand = json.loads(respons_list.text)
            for i in range(len(respons_brand)):
                data_brand[respons_brand[i]['name']] = respons_brand[i]['id'] #поменял пестами
                with open('brand.json', 'w', encoding="utf-8") as brand:
                    json.dump(data_brand, brand, indent=4, ensure_ascii=False)

    def get_model_car_list(self):
        data_model={}
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(self.brand_id) +'/models', headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_model = json.loads(respons_list.text)
            for i in range(len(respons_model)):
                data_model[respons_model[i]['name']] = respons_model[i]['id']
                with open('model.json', 'w', encoding="utf-8") as model:
                    json.dump(data_model, model, indent=4, ensure_ascii=False)

    def get_generations_car_list(self):
        data_generations={}
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(self.brand_id) +'/models/'+ str(self.model_id) +'/generations', headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_generations = json.loads(respons_list.text)
            for i in range(len(respons_generations)):
                data_generations[respons_generations[i]['name']] = respons_generations[i]['id']
                with open('generations.json', 'w', encoding="utf-8") as generations:
                    json.dump(data_generations, generations, indent=4, ensure_ascii=False)

    def __call__(self):
        self.get_brand_car_list()
        self.brand_id = self.output_car(self.brand)
        self.get_model_car_list()
        self.model_id = self.output_car('model.json')
        self.get_generations_car_list()
        self.generations_id = self.output_car('generations.json')
        return self.brand_id, self.model_id, self.generations_id

# добавить fake_useragent в headers запросов get_page_car 
# вход принимает: brand_id, model_id, generations_id
def get_page_car(*args):
    if args[0] == 0 and args[1] == 0 and args[2] == 0:
        params = {'condition[0]': 2, 'sort': 2}
    elif args[0] != 0 and args[1] == 0 and args[2] == 0:
        params = {'brands[0][brand]': args[0], 'condition[0]': 2, 'sort': 2}
    elif args[0] != 0 and args[1] != 0 and args[2] == 0:
        params = {'brands[0][brand]': args[0], 'brands[0][model]': args[1], 'condition[0]': 2, 'sort': 2}
    elif args[0] != 0 and args[1] != 0 and args[2] != 0:
        params = {'brands[0][brand]': args[0], 'brands[0][model]': args[1], 'brands[0][generation]': args[2], 'condition[0]': 2, 'sort': 2}

    page_htm = requests.get('https://cars.av.by/filter?', params=params)
    # Если страница получина, записываем данные в файл (нужно дороботать сбор со всех имеющихся страниц) + распасить и подготовить данные для оброботки
    if page_htm.status_code == 200:
        with open('page.htm', 'w', encoding="utf-8") as htm:
            data = htm.write(page_htm.text)

# get_page_car(brand_id, model_id, generations_id)
obj = Select_car()

car_crit = obj()
print(car_crit[0], car_crit[1], car_crit[2])
get_page_car(car_crit[0], car_crit[1], car_crit[2])
# Получить инфу со всех имеющихся страниц
# Распарсить инфу 
# Алгоритм анализа