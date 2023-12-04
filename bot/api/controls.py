from api.models import User, Request, Respons, db
# from api.models import User, Request, Respons, db

def reset_BD():
    '''
    Создаёт бдешку и таблицы в ней
    '''
    with db:
        db.create_tables([User, Request, Respons]) 

###########################################################USER###############################################################
def get_user_id_on_procent(percent=20, location=''):
    result_list = []
    '''
    percent !< 20
    вернет список с пользователями у которых процент ментьше 
    или равен проценту найденого авто и есоли пользователю подходит местоположение авто
    '''
    with db:
        reqest_list = User.select().where(User.percent <= percent)
    if len(reqest_list) >= 1:
        for user in reqest_list:
            locations = get_location_user(telegram_id=user.telegram_id)
            if location in locations:
                result_list.append(user)

    return result_list

def add_procent_user(telegram_id=0, percent=20):
    '''
    Добавляет percent в таблицу User
    '''
    with db:
        user = User.get(telegram_id=telegram_id)
        user.percent = percent
        user.save()

def get_location_user(telegram_id=0):
    '''
    Отдает список с location уонкретного USER по telegram_id.
    '''
    with db:
        user = User.get(telegram_id=telegram_id)
        if user.location == None:
            return []
        return user.location.split('_')

def change_location_user(telegram_id=0, location=[]):
    '''
    Изменяет текущий список location у USER
    передаем location либо новые либо старые города или все вместе.
    Можно использовать как для добавления так и для удаления элементов
    '''
    old_location = get_location_user(telegram_id=telegram_id)
    for item in location:
        if item in old_location:
            old_location.remove(item)
        else:
            old_location.append(item)

    with db:
        user = User.get(telegram_id=telegram_id)
        user.location = "_".join(list(set(old_location)))
        user.save()

def create_user(telegram_id=0):
    with db:
        return User.get_or_create(telegram_id=telegram_id)
    
def get_users():
    '''
    вернет список с tg_id пользователей
    '''
    with db:
        users = User.select()
    return users

def delet_user(telegram_id=0):
    with db:
        user = User.get(telegram_id=telegram_id)
        user.delete_instance()
###########################################################END_USER###############################################################

###########################################################REQEST###############################################################

def get_request(brand_id=0, model_id=0, generations_id=0, percent=0):
    '''
    Вернет все записи из request которым соответствует brand_id и model_id и generations_id и если percent_difference меньше или равен исеомому проценту
    '''
    with db:
        reqest_list = Request.select().where(Request.brand_id == brand_id, Request.model_id == model_id, Request.generations_id == generations_id, Request.percent_difference <= percent)
    return reqest_list

def delet_reqest(telegram_id, request_id):
    '''
    Метод удалит крнкретную запсись с параметрами для поиска
    но пред этим нужно передать в класс _request_id с помощю сетерра 
    obj.request_id = <int:и id записи>
    '''
    with db:
        user = User.get(User.telegram_id == telegram_id)
        request = Request.get(Request.user == user and Request.id == request_id)
    return request.delete_instance()

def get_sefch_data_list(telegram_id=0):
    requests_list = []
    '''
    Вeрнет поисковые параметры для конкретного пользователя
    '''
    with db:
        user = User.get(User.telegram_id == telegram_id)
        for request in user.requests:
            requests_list.append({
                    'id': request.id,
                    'brand_id':request.brand_id,
                    'model_id':request.model_id,
                    'generations_id':request.generations_id,
                    'percent_difference':request.percent_difference
                    })
    return requests_list

def create_request(brand_id=0, model_id=0, generations_id=0, percent_difference=0, telegram_id=0):
    '''
    Добавляем новые данные поиска для User
    '''
    with db:
        user = User.get(User.telegram_id == telegram_id)
        Request.get_or_create(
            brand_id=brand_id,
            model_id=model_id,
            percent_difference=percent_difference,
            generations_id=generations_id,
            user=user)
###########################################################END_REQEST###############################################################

###########################################################RESPONS###############################################################

def create_respons(link=''):
    '''
    Добавляет найденную ссылку
    '''
    with db:
        Respons.get_or_create(link=link)

def get_respons_list():
    respons_str = []
    '''
    Возвразает список найденых ссылок 
    '''
    with db:
        respons = Respons.select()

        if len(respons) >= 75:
            respons_del = respons[:25]
            for item in respons_del:
                item.delete_instance()

        for item in respons:
            respons_str.append(str(item))

    return respons_str

###########################################################END_RESPONS###############################################################


# reset_BD()

# create_user(telegram_id=0)
# create_request(brand_id=1, model_id=3, generations_id=2, percent_difference=30, telegram_id=0)
# add_procent_user(telegram_id=0, percent=50)
