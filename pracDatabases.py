from peewee import *
db=SqliteDatabase("tizi.db")

class prac(Model):
    name=TextField(unique=True)
    age=IntegerField()