from api.models import User, Respons, db # BOT
# from models import User, Respons, db # debug
import time

def reset_BD():
    '''
    Создаёт бдешку и таблицы в ней
    '''
    with db:
        db.create_tables([User, Respons]) 

###########################################################USER###############################################################
def get_user_id_on_procent(percent, location):
    result_list = []
    '''
    percent !< 20
    вернет список с пользователями у которых процент ментьше 
    или равен проценту найденого авто и есоли пользователю подходит местоположение авто
    '''
    with db:
        reqest_list = User.select().where(User.percent <= percent).where(User.is_active == True).where(User.time_sub > int(time.time()))
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

def set_is_active(telegram_id=0, active=0):
    with db:
        user = User.get(telegram_id=telegram_id)
        user.is_active = active
        user.save()

def get_is_active(telegram_id=0):
    with db:
        user = User.get(telegram_id=telegram_id)
        return user.is_active
    
###########################################################SUB###############################################################
    
def set_time_sub(telegram_id=0, time=0):
    '''Запишем время действия подписки в секуднах '''
    with db:
        user = User.get(telegram_id=telegram_id)
        user.time_sub = time
        user.save()

def get_time_sub(telegram_id=0):
    '''Вернёт время подписки в секуднах '''
    with db:
        user = User.get(telegram_id=telegram_id)
        return user.time_sub       

###########################################################END_SUB###############################################################
###########################################################END_USER###############################################################

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

# create_user(telegram_id=633279160)
# add_procent_user(telegram_id=633279160, percent=25)
