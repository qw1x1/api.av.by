import requests
from fake_useragent import UserAgent as User
from bs4 import BeautifulSoup as bs
import json
import math

class Select_car: # -> brand_id, model_id

    def __init__(self) -> None:
        self.brand_id = 0
        self.model_id = 0
        self.brand = 'brand.json'
        self.model = 'model.json'
        self.user = User().random 

    # Пока в консоль :)
    @staticmethod
    def output_car(file): # -> id
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

# вход принимает: brand_id, model_id
# def get_page_car(*args):
#     if args[0] == 0 and args[1] == 0 and args[2] == 0:
#         params = {'condition[0]': 2, 'sort': 2}
#     elif args[0] != 0 and args[1] == 0 and args[2] == 0:
#         params = {'brands[0][brand]': args[0], 'condition[0]': 2, 'sort': 2}
#     elif args[0] != 0 and args[1] != 0 and args[2] == 0:
#         params = {'brands[0][brand]': args[0], 'brands[0][model]': args[1], 'condition[0]': 2, 'sort': 2}
#     elif args[0] != 0 and args[1] != 0 and args[2] != 0:
#         params = {'brands[0][brand]': args[0], 'brands[0][model]': args[1], 'brands[0][generation]': args[2], 'condition[0]': 2, 'sort': 2}

    # page_htm = requests.get('https://cars.av.by/filter?', params=params)
    # # Если страница получина, записываем данные в файл (нужно дороботать сбор со всех имеющихся страниц) + распасить и подготовить данные для оброботки
    # if page_htm.status_code == 200:
    #     with open('page.htm', 'w', encoding="utf-8") as htm:
    #         data = htm.write(page_htm.text)


def main():
    obj = Select_car()

    car_crit = obj()
    print(car_crit[0], car_crit[1], car_crit[2])


if __name__ == "__main__":
	main()