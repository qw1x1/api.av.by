from typing import Any
from av1 import brand, Get_model, Pars_info_id_file,  Search_cars, Get_revers_model, revers_brand
from controls import Control_db
from models import *

class Get_data_for_request:
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.result_list = []
    
    def get_data(self):
        with db:
            bd = Control_db(telegram_id=self.telegram_id)
            request_list = bd.get_sefch_data_list()
        return request_list
    
    def pars_info(self):
        request_list = self.get_data()
        for item in request_list:
            data_list = Pars_info_id_file(year_min=item['year_min'], year_max=item['year_max'], price_min=item['price_min'], price_max=item['price_max'], brand_id=item['brand_id'], model_id=item['model_id'])
            obj_pars_info_id_file = data_list()
            obj_search_cars = Search_cars(car_list = obj_pars_info_id_file[0], count_page=obj_pars_info_id_file[1], deviation_procent=item['deviation_procent'])
            self.result_list.append(obj_search_cars())

    def __call__(self):
        self.pars_info()
        return self.result_list


    
        