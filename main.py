from bot.av1 import brand, Pars_info_id_file, Search_cars
from api.controls import Control_db
from api.models import *

# TEST

with db:
    obj = Control_db(12)
    # us = obj.create_user()
    # User.create(telegram_id=12)
    # us = User.get(User.telegram_id == 12)
    # re = obj.create_request(3, 3, 3, 3, 3, 3, 3, us)
    # respons_re = obj.get_sefch_data_list()
    # obj.request_id = 0
    # delet = obj.delet_reqest()
    # get_reqest = obj.get_sefch_data()
    # respons = obj.get_reqest()

# print(us)
# print(re)
# print(respons_re)
# print(delet)
# print(respons.user)
# print(obj.request_id)
# END TEST