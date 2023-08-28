from av1 import  Pars_info_id_file, Search_cars
from controls import Control_db
from models import *

class Get_data_for_request:
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.result_list = []
    
    def get_data(self):
        with db:
            bd = Control_db(telegram_id=self.telegram_id)
        return bd.get_sefch_data_list()
    
    def pars_info(self):
        search_list = self.get_data()
        for item in search_list:
            data_list = Pars_info_id_file(year_min=item['year_min'], year_max=item['year_max'], price_min=item['price_min'], price_max=item['price_max'], brand_id=item['brand_id'], model_id=item['model_id'])
            obj_pars_info_id_file = data_list()
            obj_search_cars = Search_cars(car_list = obj_pars_info_id_file[0], count_page=obj_pars_info_id_file[1], deviation_procent=item['percent_difference'])
            self.result_list.append(obj_search_cars())

    def __call__(self):
        self.pars_info()
        return self.result_list
    
# def main(): 
#     user_id = 6315832729 # message.from_user.id
#     obj = Get_data_for_request(user_id)
#     respons = obj()
#     for car in respons:
#         list_cars, arg_price = car[0], car[1]
#         for item in list_cars:
#             txt = f"Среднерыночная стоимость: {math.floor(arg_price)}  "+item['name']+f"\n"+item['lank']+f"\n"+item['parametrs']+f"\n"+item['mileage']+f"\n"+str(item['price'])+" \n"+item['description']+"\n"+item['location']
#             print(txt)
#             print()


    
# if __name__ ==  '__main__':
#     main()

    
        