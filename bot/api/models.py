from peewee import *

db = SqliteDatabase('db.sqlite')

class Basic(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
    
class User(Basic):
    telegram_id = IntegerField(unique=True)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return f'{str(self.telegram_id)}'

class Request(Basic):
    brand_id = IntegerField()
    model_id = IntegerField()
    percent_difference = IntegerField()
    year_min = IntegerField(default=1940)
    year_max = IntegerField(default=2023)
    price_min = IntegerField(default=0)
    price_max = IntegerField(default=0)
    user = ForeignKeyField(User, related_name='requests')

    class Meta:
        db_table = 'requests'

    def __str__(self):
        return f'{str(self.user.id)}'
    
