from peewee import *

db = SqliteDatabase('db_ebay.sqlite')

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
    link = TextField()
    user = ForeignKeyField(User, related_name='requests')

    class Meta:
        db_table = 'requests'

    def __str__(self):
        return f'{str(self.user.id)}'
    


