import requests
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
import json

class Select_car: # Fills in files: brand, model, generations.

    def __init__(self) -> None:
        self.brand_id = 683
        self.model_id = 5879
        self.generations_id = 4508
        self.user = User().random # Инициализация объекта UserAgent в объекте Select_car

    # Пока в консоль :)
    @staticmethod
    def output_car(file):
        with open(file, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for key, value in data.items():
                # Здесь будет вывод данных в выподающееся меню или чет того
                print(key, value)
            print()
                # Здесь бужет записоваться ответ от пользоватеоя 
            key = str(input())
            return data[key]

    def get_data_select_car(self, params, file):
        data = {}
        respons_list = requests.get('https://api.av.by/offer-types/cars/catalog/brand-items/' + params, headers={'user-agent': f'{self.user}'})
        if respons_list.status_code == 200:
            respons_data = json.loads(respons_list.text)
            for i in range(len(respons_data)):
                data[respons_data[i]['name']] = respons_data[i]['id'] 
                with open(file, 'w', encoding="utf-8") as s_file:
                    json.dump(data, s_file, indent=4, ensure_ascii=False)

    def __call__(self):
        self.get_data_select_car('', 'brand.json')
        self.brand_id = self.output_car('brand.json')
        self.get_data_select_car(str(self.brand_id) +'/models', 'model.json')
        self.model_id = self.output_car('model.json')
        self.get_data_select_car(str(self.brand_id) +'/models/'+ str(self.model_id) +'/generations' , 'generations.json')
        self.generations_id = self.output_car('generations.json')
        return self.brand_id, self.model_id, self.generations_id

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

obj = Select_car()

car_crit = obj()
print(car_crit[0], car_crit[1], car_crit[2])
# get_page_car(car_crit[0], car_crit[1], car_crit[2])