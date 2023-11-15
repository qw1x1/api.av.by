import requests, json, math
from fake_useragent import UserAgent as User
from api.controls import get_location_user, change_location_user, get_user_id_on_procent


[{'id': 1001, 'region_name': 'Брестская обл.', 'goroda':[]},
{'id': 1002, 'region_name': 'Витебская обл.', 'goroda':[]},
{'id': 1003, 'region_name': 'Гомельская обл.', 'goroda':[]}, 
{'id': 1004, 'region_name': 'Гродненская обл.', 'goroda':[]},
{'id': 1005, 'region_name': 'Минская обл.', 'goroda':[]}, 
{'id': 1006, 'region_name': 'Могилевская обл.', 'goroda':[]}]

[{'city_name': 'Брест', 'id': 8},
{'city_name': 'Барановичи', 'id': 116},
{'city_name': 'Белоозёрск', 'id': 796},
{'city_name': 'Береза', 'id': 117},
{'city_name': 'Высокое', 'id': 797},
{'city_name': 'Ганцевичи', 'id': 118},
{'city_name': 'Давид-Городок', 'id': 790},
{'city_name': 'Дрогичин', 'id': 119},
{'city_name': 'Жабинка', 'id': 120},
{'city_name': 'Иваново', 'id': 121}, 
{'city_name': 'Ивацевичи', 'id': 122},
{'city_name': 'Каменец', 'id': 123},
{'city_name': 'Кобрин', 'id': 124}, 
{'city_name': 'Коссово', 'id': 798},
{'city_name': 'Лунинец', 'id': 125},
{'city_name': 'Ляховичи', 'id': 126},
{'city_name': 'Малорита', 'id': 127},
{'city_name': 'Микашевичи', 'id': 789},
{'city_name': 'Пинск', 'id': 128}, 
{'city_name': 'Пружаны', 'id': 129}, 
{'city_name': 'Столин', 'id': 130}]

[{'city_name': 'Витебск', 'id': 7},
{'city_name': 'Барань', 'id': 792},
{'city_name': 'Бешенковичи', 'id': 131}, 
{'city_name': 'Браслав', 'id': 132},
{'city_name': 'Верхнедвинск', 'id': 133},
{'city_name': 'Глубокое', 'id': 134}, 
{'city_name': 'Городок', 'id': 135},
{'city_name': 'Дисна', 'id': 793}, 
{'city_name': 'Докшицы', 'id': 136},
{'city_name': 'Дубровно', 'id': 137},
{'city_name': 'Лепель', 'id': 138},
{'city_name': 'Лиозно', 'id': 139}, 
{'city_name': 'Миоры', 'id': 140},
{'city_name': 'Новолукомль', 'id': 791},
{'city_name': 'Новополоцк', 'id': 141},
{'city_name': 'Орша', 'id': 142},
{'city_name': 'Полоцк', 'id': 143},
{'city_name': 'Поставы', 'id': 144},
{'city_name': 'Россоны', 'id': 145},
{'city_name': 'Сенно', 'id': 146},
{'city_name': 'Толочин', 'id': 147},
{'city_name': 'Ушачи', 'id': 148},
{'city_name': 'Чашники', 'id': 149}, 
{'city_name': 'Шарковщина', 'id': 150},
{'city_name': 'Шумилино', 'id': 151}]

[{'city_name': 'Гомель', 'id': 9},
{'city_name': 'Брагин', 'id': 152},
{'city_name': 'Буда-Кошелево', 'id': 153},
{'city_name': 'Василевичи', 'id': 794},
{'city_name': 'Ветка', 'id': 154},
{'city_name': 'Добруш', 'id': 155},
{'city_name': 'Ельск', 'id': 156},
{'city_name': 'Житковичи', 'id': 157},
{'city_name': 'Жлобин', 'id': 158},
{'city_name': 'Калинковичи', 'id': 159},
{'city_name': 'Корма', 'id': 161},
{'city_name': 'Лельчицы', 'id': 162},
{'city_name': 'Лоев', 'id': 163}, 
{'city_name': 'Мозырь', 'id': 164}, 
{'city_name': 'Наровля', 'id': 165},
{'city_name': 'Октябрьский', 'id': 166},
{'city_name': 'Петриков', 'id': 167},
{'city_name': 'Речица', 'id': 168}, 
{'city_name': 'Рогачев', 'id': 169},
{'city_name': 'Светлогорск', 'id': 170},
{'city_name': 'Сосновый Бор', 'id': 803}, 
{'city_name': 'Туров', 'id': 795},
{'city_name': 'Хойники', 'id': 172},
{'city_name': 'Чечерск', 'id': 171}]

[{'city_name': 'Гродно', 'id': 3},
{'city_name': 'Берёзовка', 'id': 800},
{'city_name': 'Большая Берестовица', 'id': 173},
{'city_name': 'Волковыск', 'id': 174}, 
{'city_name': 'Вороново', 'id': 175},
{'city_name': 'Дятлово', 'id': 176},
{'city_name': 'Зельва', 'id': 177},
{'city_name': 'Ивье', 'id': 178},
{'city_name': 'Кореличи', 'id': 179},
{'city_name': 'Лида', 'id': 180},
{'city_name': 'Мосты', 'id': 181}, 
{'city_name': 'Новогрудок', 'id': 182}, 
{'city_name': 'Островец', 'id': 183}, 
{'city_name': 'Ошмяны', 'id': 184},
{'city_name': 'Свислочь', 'id': 185}, 
{'city_name': 'Скидель', 'id': 799},
{'city_name': 'Слоним', 'id': 186}, 
{'city_name': 'Сморгонь', 'id': 187},
{'city_name': 'Щучин', 'id': 188},
{'city_name': 'Россь', 'id': 806}]

[{'city_name': 'Минск', 'id': 2}, 
{'city_name': 'Березино', 'id': 92},
{'city_name': 'Борисов', 'id': 93},
{'city_name': 'Вилейка', 'id': 94},
{'city_name': 'Воложин', 'id': 95},
{'city_name': 'Дзержинск', 'id': 96},
{'city_name': 'Жодино', 'id': 97}, 
{'city_name': 'Заславль', 'id': 98},
{'city_name': 'Клецк', 'id': 99},
{'city_name': 'Копыль', 'id': 100},
{'city_name': 'Крупки', 'id': 101},
{'city_name': 'Логойск', 'id': 102},
{'city_name': 'Любань', 'id': 103},
{'city_name': 'Марьина Горка', 'id': 104},
{'city_name': 'Михановичи', 'id': 804},
{'city_name': 'Молодечно', 'id': 105},
{'city_name': 'Мядель', 'id': 106},
{'city_name': 'Несвиж', 'id': 107},
{'city_name': 'Прилуки', 'id': 805},
{'city_name': 'Пуховичи', 'id': 108},
{'city_name': 'Раков', 'id': 788},
{'city_name': 'Руденск', 'id': 248},
{'city_name': 'Слуцк', 'id': 109},
{'city_name': 'Смолевичи', 'id': 110},
{'city_name': 'Солигорск', 'id': 111},
{'city_name': 'Старые Дороги', 'id': 112},
{'city_name': 'Столбцы', 'id': 113},
{'city_name': 'Узда', 'id': 114},
{'city_name': 'Фаниполь', 'id': 160},
{'city_name': 'Червень', 'id': 115}]

[{'city_name': 'Могилев', 'id': 6},
{'city_name': 'Белыничи', 'id': 189},
{'city_name': 'Бобруйск', 'id': 190},
{'city_name': 'Быхов', 'id': 191},
{'city_name': 'Глуск', 'id': 192},
{'city_name': 'Горки', 'id': 193},
{'city_name': 'Дрибин', 'id': 194},
{'city_name': 'Кировск', 'id': 195},
{'city_name': 'Климовичи', 'id': 196},
{'city_name': 'Кличев', 'id': 197},
{'city_name': 'Костюковичи', 'id': 198},
{'city_name': 'Краснополье', 'id': 199}, 
{'city_name': 'Кричев', 'id': 200}, 
{'city_name': 'Круглое', 'id': 201},
{'city_name': 'Мстиславль', 'id': 202},
{'city_name': 'Осиповичи', 'id': 203},
{'city_name': 'Славгород', 'id': 204},
{'city_name': 'Хотимск', 'id': 205},
{'city_name': 'Чаусы', 'id': 206}, 
{'city_name': 'Чериков', 'id': 207},
{'city_name': 'Шклов', 'id': 208}]

CITY_IN_REGION = [
{'id': 0, 'region_name': 'Брестская обл.', 'city':[
    {'city_name': 'Брест', 'id': 8},
    {'city_name': 'Барановичи', 'id': 116},
    {'city_name': 'Белоозёрск', 'id': 796},
    {'city_name': 'Береза', 'id': 117},
    {'city_name': 'Высокое', 'id': 797},
    {'city_name': 'Ганцевичи', 'id': 118},
    {'city_name': 'Давид-Городок', 'id': 790},
    {'city_name': 'Дрогичин', 'id': 119},
    {'city_name': 'Жабинка', 'id': 120},
    {'city_name': 'Иваново', 'id': 121}, 
    {'city_name': 'Ивацевичи', 'id': 122},
    {'city_name': 'Каменец', 'id': 123},
    {'city_name': 'Кобрин', 'id': 124}, 
    {'city_name': 'Коссово', 'id': 798},
    {'city_name': 'Лунинец', 'id': 125},
    {'city_name': 'Ляховичи', 'id': 126},
    {'city_name': 'Малорита', 'id': 127},
    {'city_name': 'Микашевичи', 'id': 789},
    {'city_name': 'Пинск', 'id': 128}, 
    {'city_name': 'Пружаны', 'id': 129}, 
    {'city_name': 'Столин', 'id': 130}]},
{'id': 1, 'region_name': 'Витебская обл.', 'city':[
    {'city_name': 'Витебск', 'id': 7},
    {'city_name': 'Барань', 'id': 792},
    {'city_name': 'Бешенковичи', 'id': 131}, 
    {'city_name': 'Браслав', 'id': 132},
    {'city_name': 'Верхнедвинск', 'id': 133},
    {'city_name': 'Глубокое', 'id': 134}, 
    {'city_name': 'Городок', 'id': 135},
    {'city_name': 'Дисна', 'id': 793}, 
    {'city_name': 'Докшицы', 'id': 136},
    {'city_name': 'Дубровно', 'id': 137},
    {'city_name': 'Лепель', 'id': 138},
    {'city_name': 'Лиозно', 'id': 139}, 
    {'city_name': 'Миоры', 'id': 140},
    {'city_name': 'Новолукомль', 'id': 791},
    {'city_name': 'Новополоцк', 'id': 141},
    {'city_name': 'Орша', 'id': 142},
    {'city_name': 'Полоцк', 'id': 143},
    {'city_name': 'Поставы', 'id': 144},
    {'city_name': 'Россоны', 'id': 145},
    {'city_name': 'Сенно', 'id': 146},
    {'city_name': 'Толочин', 'id': 147},
    {'city_name': 'Ушачи', 'id': 148},
    {'city_name': 'Чашники', 'id': 149}, 
    {'city_name': 'Шарковщина', 'id': 150},
    {'city_name': 'Шумилино', 'id': 151}]},
{'id': 2, 'region_name': 'Гомельская обл.', 'city':[
    {'city_name': 'Гомель', 'id': 9},
    {'city_name': 'Брагин', 'id': 152},
    {'city_name': 'Буда-Кошелево', 'id': 153},
    {'city_name': 'Василевичи', 'id': 794},
    {'city_name': 'Ветка', 'id': 154},
    {'city_name': 'Добруш', 'id': 155},
    {'city_name': 'Ельск', 'id': 156},
    {'city_name': 'Житковичи', 'id': 157},
    {'city_name': 'Жлобин', 'id': 158},
    {'city_name': 'Калинковичи', 'id': 159},
    {'city_name': 'Корма', 'id': 161},
    {'city_name': 'Лельчицы', 'id': 162},
    {'city_name': 'Лоев', 'id': 163}, 
    {'city_name': 'Мозырь', 'id': 164}, 
    {'city_name': 'Наровля', 'id': 165},
    {'city_name': 'Октябрьский', 'id': 166},
    {'city_name': 'Петриков', 'id': 167},
    {'city_name': 'Речица', 'id': 168}, 
    {'city_name': 'Рогачев', 'id': 169},
    {'city_name': 'Светлогорск', 'id': 170},
    {'city_name': 'Сосновый Бор', 'id': 803}, 
    {'city_name': 'Туров', 'id': 795},
    {'city_name': 'Хойники', 'id': 172},
    {'city_name': 'Чечерск', 'id': 171}]}, 
{'id': 3, 'region_name': 'Гродненская обл.', 'city':[
    {'city_name': 'Гродно', 'id': 3},
    {'city_name': 'Берёзовка', 'id': 800},
    {'city_name': 'Большая Берестовица', 'id': 173},
    {'city_name': 'Волковыск', 'id': 174}, 
    {'city_name': 'Вороново', 'id': 175},
    {'city_name': 'Дятлово', 'id': 176},
    {'city_name': 'Зельва', 'id': 177},
    {'city_name': 'Ивье', 'id': 178},
    {'city_name': 'Кореличи', 'id': 179},
    {'city_name': 'Лида', 'id': 180},
    {'city_name': 'Мосты', 'id': 181}, 
    {'city_name': 'Новогрудок', 'id': 182}, 
    {'city_name': 'Островец', 'id': 183}, 
    {'city_name': 'Ошмяны', 'id': 184},
    {'city_name': 'Свислочь', 'id': 185}, 
    {'city_name': 'Скидель', 'id': 799},
    {'city_name': 'Слоним', 'id': 186}, 
    {'city_name': 'Сморгонь', 'id': 187},
    {'city_name': 'Щучин', 'id': 188},
    {'city_name': 'Россь', 'id': 806}]},
{'id': 4, 'region_name': 'Минская обл.', 'city':[
    {'city_name': 'Минск', 'id': 2}, 
    {'city_name': 'Березино', 'id': 92},
    {'city_name': 'Борисов', 'id': 93},
    {'city_name': 'Вилейка', 'id': 94},
    {'city_name': 'Воложин', 'id': 95},
    {'city_name': 'Дзержинск', 'id': 96},
    {'city_name': 'Жодино', 'id': 97}, 
    {'city_name': 'Заславль', 'id': 98},
    {'city_name': 'Клецк', 'id': 99},
    {'city_name': 'Копыль', 'id': 100},
    {'city_name': 'Крупки', 'id': 101},
    {'city_name': 'Логойск', 'id': 102},
    {'city_name': 'Любань', 'id': 103},
    {'city_name': 'Марьина Горка', 'id': 104},
    {'city_name': 'Михановичи', 'id': 804},
    {'city_name': 'Молодечно', 'id': 105},
    {'city_name': 'Мядель', 'id': 106},
    {'city_name': 'Несвиж', 'id': 107},
    {'city_name': 'Прилуки', 'id': 805},
    {'city_name': 'Пуховичи', 'id': 108},
    {'city_name': 'Раков', 'id': 788},
    {'city_name': 'Руденск', 'id': 248},
    {'city_name': 'Слуцк', 'id': 109},
    {'city_name': 'Смолевичи', 'id': 110},
    {'city_name': 'Солигорск', 'id': 111},
    {'city_name': 'Старые Дороги', 'id': 112},
    {'city_name': 'Столбцы', 'id': 113},
    {'city_name': 'Узда', 'id': 114},
    {'city_name': 'Фаниполь', 'id': 160},
    {'city_name': 'Червень', 'id': 115}]}, 
{'id': 5, 'region_name': 'Могилевская обл.', 'city':[
    {'city_name': 'Могилев', 'id': 6},
    {'city_name': 'Белыничи', 'id': 189},
    {'city_name': 'Бобруйск', 'id': 190},
    {'city_name': 'Быхов', 'id': 191},
    {'city_name': 'Глуск', 'id': 192},
    {'city_name': 'Горки', 'id': 193},
    {'city_name': 'Дрибин', 'id': 194},
    {'city_name': 'Кировск', 'id': 195},
    {'city_name': 'Климовичи', 'id': 196},
    {'city_name': 'Кличев', 'id': 197},
    {'city_name': 'Костюковичи', 'id': 198},
    {'city_name': 'Краснополье', 'id': 199}, 
    {'city_name': 'Кричев', 'id': 200}, 
    {'city_name': 'Круглое', 'id': 201},
    {'city_name': 'Мстиславль', 'id': 202},
    {'city_name': 'Осиповичи', 'id': 203},
    {'city_name': 'Славгород', 'id': 204},
    {'city_name': 'Хотимск', 'id': 205},
    {'city_name': 'Чаусы', 'id': 206}, 
    {'city_name': 'Чериков', 'id': 207},
    {'city_name': 'Шклов', 'id': 208}]}
]


#######################################
def get_region():
    '''
    Возвращает список областей
    # бот выводит назвнаия областей и отдаёт 'id' 
    '''
    region = []
    for region_dikt in CITY_IN_REGION:
        region.append({region_dikt['region_name']:region_dikt['id']})
    return region

def get_city_for_region(region_id):
    '''Возвращает список городов в конкретной области по id области'''
    city = []
    for city_dikt in CITY_IN_REGION[region_id]['city']:
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
