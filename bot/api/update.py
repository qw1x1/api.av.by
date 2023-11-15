from api.av1 import Pars_info_id_file, Search_cars
from api.controls import get_sefch_data_list
  
def pars_info(search_list):
    '''
    Передаём список с диетом или диктами  {'brand':brand_id, 'model':model_id, 'generations_id':generations_id,  'percent_difference': percent_difference}
    Получаем список с машинами с больщим или такимже percent_difference
    '''
    result_list = []

    for item in search_list:
        data_list = Pars_info_id_file(brand_id=item['brand_id'], model_id=item['model_id'], generations_id=item['generations_id'])
        obj_pars_info_id_file = data_list()
        obj_search_cars = Search_cars(car_list = obj_pars_info_id_file[0], count_page=obj_pars_info_id_file[1], deviation_procent=item['percent_difference'])
        result_list.append(obj_search_cars())
    return result_list

search_list = get_sefch_data_list(telegram_id=121)
pars_info(search_list)