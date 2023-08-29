from api.models import User, Request

class Control_db():
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.requests_list = []
        self._request_id = None

    @property 
    def request_id(self):   
        return self._request_id

    @request_id.setter  
    def request_id(self, request_id):   
        self._request_id = request_id

    def create_user(self):
        return User.get_or_create(telegram_id=self.telegram_id)
            
    @staticmethod
    def create_request(brand_id=0, model_id=0, percent_difference=0, year_min=0, year_max=0, price_min=0, price_max=0, user=0):
        '''
        Добавляем новые данные поиска для User
        '''
        Request.get_or_create(
            brand_id=brand_id,
            model_id=model_id,
            percent_difference=percent_difference,
            year_min=year_min,
            year_max=year_max,
            price_min=price_min,
            price_max=price_max,
            user=user)
    
    def get_sefch_data_list(self):
        '''
        Вкрнет поисковые параметры для конкретного пользователя
        '''
        user = User.get(User.telegram_id == self.telegram_id)
        for request in user.requests:
            self.requests_list.append({
                    'id': request.id,
                    'brand_id':request.brand_id,
                    'model_id':request.model_id,
                    'percent_difference':request.percent_difference,
                    'year_min':request.year_min,
                    'year_max':request.year_max,
                    'price_min':request.price_min,
                    'price_max':request.price_max
                    })
        return self.requests_list

    def delet_reqest(self):
        '''
        Метод удалит крнкретную запсись с параметрами для поиска
        но пред этим нужно передать в класс _request_id с помощю сетерра 
        obj.request_id = <int:и id записи>
        '''
        user = User.get(User.telegram_id == self.telegram_id)
        request = Request.get(Request.user == user and Request.id == self._request_id)
        return request.delete_instance()

def get_users():
    '''
    вернет список с tg_id пользователей
    '''
    users = User.select()
    return users