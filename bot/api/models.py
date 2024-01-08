from peewee import *

db = SqliteDatabase('db.sqlite')

class Basic(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
    
class User(Basic):
    telegram_id = IntegerField(unique=True)
    percent = IntegerField(null=True)
    location = CharField(null=True)
    is_active = BooleanField(null=True, default = 0) # Если True, то выполняется поиск для этого пользователя, иначе поиск остановлен
    time_sub = IntegerField(null=True, default = 0) # Если True, то у пользователя оплачена подписка и поиск для него работает, иначе поиск остановлен

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return f'{str(self.telegram_id)}'
    
class Respons(Basic):
    link = CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'respons'

    def __str__(self):
        return f'{str(self.link)}'
