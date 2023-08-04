import requests
from bs4 import BeautifulSoup as bs
import json

brand_id = 683 # mersedec-benz
model_id = 5879 # C-class
generations_id = 4508 # 202 - 1 generations

class Select_car: # Fills in files: brand, model, generations.
    def __init__(self) -> None:
        '''
            Вывод скисков
            Получение последовательных ответов (ВАЖНО СОБЛЮДАТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ)
            
        '''
        self.brand_id = 0
        self.model_id = 0
        self.generations_id = 0

    def get_brand_car_list(self):
        brand_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items')
        data_brand = json.loads(brand_list.text)
        with open('brand.json', 'w') as brand:
            json.dump(data_brand, brand)
            
    def get_model_car_list(self):
        model_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models')
        data_model = json.loads(model_list.text)
        with open('model.json', 'w') as model:
            json.dump(data_model, model)

    def get_generations_car_list(self):
        generations_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/'+ str(brand_id) +'/models/'+ str(model_id) +'/generations')
        data_generations = json.loads(generations_list.text)
        with open('generations.json', 'w') as generations:
            json.dump(data_generations, generations)

    def __call__(self):
        self.get_brand_car_list()
        self.get_model_car()
        self.get_generations_car()

# obj = Select_car()
# obj()


def get_page_car(brand_id, model_id, generations_id):
    page_htm = requests.get('https://cars.av.by/filter?', {'brands[0][brand]': brand_id, 'brands[0][model]': model_id, 'brands[0][generation]': generations_id, 'condition[0]': 2, 'sort': 2})
    if page_htm.status_code == 200:
        with open('page.htm', 'w', encoding="utf-8") as htm:
            data = htm.write(page_htm.text)

get_page_car(brand_id, model_id, generations_id)