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
        self.brand_id = 0
        self.model_id = 0
        self.generations_id = 0
        self.user = User().random # Инициализация объекта UserAgent в объекте Select_car

    def get_brand_car_list(self):
        brand_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items', headers={'user-agent': f'{self.user}'})
        data_brand = json.loads(brand_list.text)
        with open('brand.json', 'w', encoding="utf-8") as brand:
            json.dump(data_brand, brand, indent=4, ensure_ascii=False)
            
    def get_model_car_list(self):
        model_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models', headers={'user-agent': f'{self.user}'})
        data_model = json.loads(model_list.text)
        with open('model.json', 'w', encoding="utf-8") as model:
            json.dump(data_model, model, indent=4, ensure_ascii=False)

    def get_generations_car_list(self):
        generations_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models/'+ str(model_id) +'/generations', headers={'user-agent': f'{self.user}'})
        data_generations = json.loads(generations_list.text)
        with open('generations.json', 'w', encoding="utf-8") as generations:
            json.dump(data_generations, generations, indent=4, ensure_ascii=False)

    def __call__(self):
        self.get_brand_car_list()
        self.get_model_car_list()
        self.get_generations_car_list()

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

get_page_car(brand_id, model_id, generations_id)
obj = Select_car()
obj()
# Получить инфу со всех имеющихся страниц
# Распарсить инфу 
# Алгоритм анализа