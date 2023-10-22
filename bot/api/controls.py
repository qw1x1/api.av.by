from models import User, Request, Respons, db
# from models import User, Request, db

###########################################################USER###############################################################
def get_user_id_on_procent(percent=20):
    '''
    percent !< 20
    вернет список с пользователями у которых процент ментьше или равен проценту найденого авто
    '''
    with db:
        reqest_list = User.select().where(User.percent <= percent)
    return reqest_list

def add_procent_user(telegram_id=0, percent=20):
    '''Если пользователь уже создан, но он не перекуп и у него нет percent,
    то мы добавляем его 
    '''
    with db:
        user = User.get(telegram_id=telegram_id)
        user.percent = percent
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

def get_sefch_data_list(telegram_id):
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
def create_respons(link='', telegram_id=0):
    '''
    Добавляет отправленные ссылки для конкретного пользователя
    '''
    link_str = '_'.join(link)
    with db:
        user = User.get(telegram_id=telegram_id)
        Respons.get_or_create(
            links=link_str,
            user=user)

def get_respons_list(telegram_id=0):
    '''
    Возвразает список отправленных ссылок пользователю
    '''
    respons_list = []
    respp = []
    with db:
        user = User.get(User.telegram_id == telegram_id)
        for respons in user.respons:
            respons_list.append(respons.links)

        for item in respons_list:
            respp.append(item.split('_'))
    return respp
  
def del_all_respons():
    '''
    Удаляет все записи у всех пользователей
    '''
    pass
###########################################################END_RESPONS###############################################################

# with db:
#     db.create_tables([User, Request, Respons])
#     create_user(telegram_id=633279160)
# create_request(brand_id=1, model_id=3, generations_id=0, percent_difference=30, telegram_id=633279160)
# add_procent_user(telegram_id=633279160, percent=50)