from models import User, Request, db

def create_user(telegram_id=1212121212,):
    with db:
        return User.get_or_create(telegram_id=telegram_id)
    
def get_users():
    '''
    вернет список с tg_id пользователей
    '''
    with db:
        users = User.select()
    return users

def delet_reqest(telegram_id, request_id):
    '''
    Метод удалит крнкретную запсись с параметрами для поиска
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
                    'link':request.link,
                    })
    return requests_list

def create_request(link='', user=0):
    '''
    Добавляем новые данные поиска для User
    '''
    with db:
        Request.get_or_create(
            link=link,
            user=user)
##########################################################################################################################

# with db:
#     db.create_tables([User, Request])
    # create_user(222)
    # create_request(link='https://www.kleinanzeigen.de/s-autoteile-reifen/wuppertal/c223l1561r20', user=2)


