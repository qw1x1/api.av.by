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


# Мб пок не юзаю но может пригодиться
class Integer:
    @classmethod
    def is_valid_data(cls, value):
        if type(value) != int:
            return 0 
        return value
 
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        self.is_valid_data(value)
        instance.__dict__[self.name] = value

class Create_request(): 
    brand_id = Integer() 
    model_id = Integer()  
    percent_difference = Integer()
    year_min = Integer() 
    year_max = Integer() 
    price_min = Integer() 
    price_max = Integer() 

    def __init__(self, telegram_id, brand_id = 0, model_id = 0, percent_difference = 1, year_min = 0, year_max = 0, price_min = 0, price_max = 0):
        self.brand_id = brand_id
        self.model_id = model_id 
        self.percent_difference = percent_difference 
        self.year_min = year_min
        self.year_max = year_max
        self.price_min = price_min
        self.price_max = price_max
        self.user = Control_db(telegram_id).create_user()

    def create_request(self):
        '''
        Добавляем новые данные поиска для User
        '''
        Request.create(
            brand_id=self.brand_id,
            model_id=self.model_id,
            percent_difference=self.percent_difference,
            year_min=self.year_min,
            year_max=self.year_max,
            price_min=self.price_min,
            price_max=self.price_max,
            user=self.user
            )
        
# Мб пок не юзаю но может пригодиться