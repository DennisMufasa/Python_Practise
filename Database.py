# import all methods from the peewee library
from peewee import *

# create an instance of SQLite database class
database=SqliteDatabase("mufasa.db")

# create a  class that will create a table when invoked(line 16)
class Person(Model):
    name=TextField()
    age=IntegerField()
    profession=TextField()
# create a meta class inside the model class
    class Meta:
        database=database

# Person.create_table()

# after running line 16, comment it to prevent the program from creating a new table everytime the code runs.

# populating the table
# Person.create(name="Denny",age=23,profession="Developer")
# Person.create(name="Vicky",age=23,profession="IT")
# Person.create(name="Jay",age=25,profession="Chef")

# fetch data from database
# details=Person.get(id=3)
# print(details.name,' is a',details.profession)

# selecting data from database
# select=Person.select()
# for i in select:
#     print(i.name)
