from models import User, Request, db
# from models import User, Request, db

##########################################################################################################################
def get_user_id_on_procent(percent=0):
    '''
    вернет список с пользователями у которых процент ментьше или равен проценту найденого авто
    '''
    with db:
        reqest_list = User.select().where(User.percent <= percent)
    return reqest_list

def add_procent_user(telegram_id=0, percent=1):
    '''Если пользователь уже создан, но он не перекуп и у него нет percent,
    то мы добавляем его 
    '''
    with db:
        user = User.get(telegram_id=telegram_id)
        user.percent = percent
        user.save()

def create_user(telegram_id=1212121212, percent=0):
    with db:
        return User.get_or_create(telegram_id=telegram_id, percent=percent)
    
def get_users():
    '''
    вернет список с tg_id пользователей
    '''
    with db:
        users = User.select()
    return users

def get_request(brand_id=0, model_id=0, percent=0):
    '''
    Вернет все записи из request которым соответствует brand_id и model_id и если percent_difference меньше или равен исеомому проценту
    '''
    with db:
        reqest_list = Request.select().where(Request.brand_id == brand_id, Request.model_id == model_id, Request.percent_difference <= percent)
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
    Вкрнет поисковые параметры для конкретного пользователя
    '''
    with db:
        user = User.get(User.telegram_id == telegram_id)
        for request in user.requests:
            requests_list.append({
                    'id': request.id,
                    'brand_id':request.brand_id,
                    'model_id':request.model_id,
                    'percent_difference':request.percent_difference,
                    'year_min':request.year_min,
                    'year_max':request.year_max,
                    'price_min':request.price_min,
                    'price_max':request.price_max
                    })
    return requests_list

def create_request(brand_id=0, model_id=0, percent_difference=0, year_min=0, year_max=0, price_min=0, price_max=0, user=0):
    '''
    Добавляем новые данные поиска для User
    '''
    with db:
        Request.get_or_create(
            brand_id=brand_id,
            model_id=model_id,
            percent_difference=percent_difference,
            year_min=year_min,
            year_max=year_max,
            price_min=price_min,
            price_max=price_max,
            user=user)
##########################################################################################################################

# with db:
    # db.create_tables([User, Request])
    # create_request(telegram_id=11, percent=1)
    # create_request(brand_id=0, model_id=0, percent_difference=0, year_min=0, year_max=0, price_min=0, price_max=0, user=1)
# add_procent_user(telegram_id=12, percent=50)
# 

