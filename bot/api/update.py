from api.av1 import  Pars_info_id_file, Search_cars
from api.controls import *
from api.models import *

class Get_data_for_request:
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.result_list = []
    
    def get_data(self):
        return get_sefch_data_list(self.telegram_id)
    
    def pars_info(self):
        search_list = self.get_data()
        for item in search_list:
            data_list = Pars_info_id_file(brand_id=item['brand_id'], model_id=item['model_id'], generations_id=item['generations_id'])
            obj_pars_info_id_file = data_list()
            obj_search_cars = Search_cars(car_list = obj_pars_info_id_file[0], count_page=obj_pars_info_id_file[1], deviation_procent=item['percent_difference'])
            self.result_list.append(obj_search_cars())

    def __call__(self):
        self.pars_info()
        return self.result_list