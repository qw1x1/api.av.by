from peewee import *

db = SqliteDatabase('db.sqlite')

class Basic(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
    
class User(Basic):
    telegram_id = IntegerField(unique=True)
    percent = IntegerField()

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return f'{str(self.telegram_id)}'

class Request(Basic):
    brand_id = IntegerField()
    model_id = IntegerField()
    generations_id = IntegerField()
    percent_difference = IntegerField()
    user = ForeignKeyField(User, related_name='requests')

    class Meta:
        db_table = 'requests'

    def __str__(self):
        return f'{str(self.user.id)}'
    
class Respons(Basic):
    links = TextField()
    user = ForeignKeyField(User, related_name='respons')

    class Meta:
        db_table = 'respons'

    def __str__(self):
        return f'{str(22)}'


