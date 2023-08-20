from api.models import db, User, Request

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
        '''
        Если пользователь уже создан return User
        '''
        if User.get(User.telegram_id == self.telegram_id):
            return User.get(User.telegram_id == self.telegram_id)
        else:
            User.create(telegram_id=self.telegram_id)
            return User.get(User.telegram_id == self.telegram_id)
            
    @staticmethod
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

    def get_sefch_data_list(self):
        '''
        Вкрнет поисковые параметры для конкретного пользователя
        '''
        user = User.get(User.telegram_id == self.telegram_id)
        for request in user.requests:
            self.requests_list.append({
                    'brand_id':request.brand_id,
                    'model_id':request.model_id,
                    'percent_difference':request.percent_difference,
                    'year_min':request.year_min,
                    'year_max':request.year_max,
                    'price_min':request.price_min,
                    'price_max':request.price_max
                    })
        return self.requests_list
    
    def get_reqest(self):
        '''
        Метод вернет крнкретную запсись с параметрами для поиска
        но пред этим нужно передать в класс _request_id с помощю сетерра 
        obj.request_id = <int:и id записи>
        '''
        user = User.get(User.telegram_id == self.telegram_id)
        return user.requests[self._request_id]
    

    def delet_reqest(self):
        '''
        Метод удалит крнкретную запсись с параметрами для поиска
        но пред этим нужно передать в класс _request_id с помощю сетерра 
        obj.request_id = <int:и id записи>
        '''
        user = User.get(User.telegram_id == self.telegram_id)
        return user.requests[self._request_id].delete_instance()

