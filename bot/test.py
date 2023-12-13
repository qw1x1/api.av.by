import requests, json, math
from fake_useragent import UserAgent as User
from api.controls import get_location_user, change_location_user, get_user_id_on_procent7
from bot.settings import CITY_IN_REGION as REGION

#######################################
def get_region():
    '''
    Возвращает список областей
    # бот выводит назвнаия областей и отдаёт 'id' 
    '''
    region = []
    for region_dikt in REGION:
        region.append({region_dikt['region_name']:region_dikt['id']})
    return region

def get_city_for_region(region_id):
    '''Возвращает список городов в конкретной области по id области'''
    city = []
    for city_dikt in REGION[region_id]['city']:
        city.append({city_dikt['city_name']:city_dikt['id']})
    return city
#######################################



# change_location_user(telegram_id=0, location=['Барановичи', 'Брест', 'Белоозёрск', 'Береза'])
# change_locat = change_location_user(telegram_id=0, location=['Брест'])
# locals = get_location_user(telegram_id=0)

# regio = get_region()
# reg = get_city_for_region(0)
# set_city()

# print(regio)
# print(reg)
# print(locals)
# print(change_locat)





# users = get_user_id_on_procent(percent=40, location='Брест')
# print(users)
