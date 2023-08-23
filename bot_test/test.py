from av1 import brand, Pars_info_id_file, Search_cars
from controls import Control_db
from models import *

# TEST

with db:
    obj = Control_db(6315832729)
    us = obj.create_user()

#     re = obj.create_request(brand_id=1, model_id=0, percent_difference=0, year_min=0, year_max=0, price_min=0, price_max=0, user=us[0])
    respons_re = obj.get_sefch_data_list()
    # obj.request_id = 0
    # delet = obj.delet_reqest()
    # get_reqest = obj.get_sefch_data()
    # respons = obj.get_reqest()

# print(us)
# print(re)
print(respons_re[1]['id'])
# print(delet)
# print(us)
# print(obj.request_id)
# END TEST
