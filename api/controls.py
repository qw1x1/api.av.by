from models import User, Request

def create_user(telegram_id):
    '''
    Если пользователь уже создан return User
    '''
    if User.get(User.telegram_id == telegram_id):
        return User.get(User.telegram_id == telegram_id)
    else:
        User.create(telegram_id=telegram_id)
        return User.get(User.telegram_id == telegram_id)

def create_request(brand_id, model_id, percent_difference, year_min, year_max, price_min, price_max, user):
    '''
    Добавляем новые данные поиска для User
    '''
    Request.create(
        brand_id=brand_id,
        model_id=model_id,
        percent_difference=percent_difference,
        year_min=year_min,
        year_max=year_max,
        price_min=price_min,
        price_max=price_max,
        user=user
        )

def get_sefch_data(telegram_id):
    '''
    Вкрнет поисковые параметры для конкретного пользователя
    '''
    requests_list = []
    user = User.get(User.telegram_id == telegram_id)
    for request in user.requests:
        requests_list.append({
                'brand_id':request.brand_id,
                'model_id':request.model_id,
                'percent_difference':request.percent_difference,
                'year_min':request.year_min,
                'year_max':request.year_max,
                'price_min':request.price_min,
                'price_max':request.price_max
                })
    return requests_list