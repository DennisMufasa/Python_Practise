"""Import peewee library"""
from peewee import *
"""create an instance of the Sqlite database"""
db = SqliteDatabase('emobilis.db')      # Accepts the database name as a parameter
"""create a model class for the table in the database"""
class Students(Model):
    """Creating table_fields variables"""
    adm_no = IntegerField()
    first_name = TextField()
    last_name = TextField()
    course = TextField()
    """create a meta class"""
    class Meta:
        database = db


# Up until this point the database has not been created i.e If you run the code above ALONE nothing happens

"""create the table (and in turn database)"""
#Students.create_table()

# Run the code above first then comment the line before proceeding.

"""populate the table with some dummy data(Insert)"""
# Students.create(adm_no=1422,first_name='Viv',last_name='Wanja',course='Pyhton')
# Students.create(adm_no=1368,first_name='Bret',last_name='Williams',course='Cyhton')
# Students.create(adm_no=1410,first_name='Rot',last_name='Hier',course='PHP')
# Students.create(adm_no=1340,first_name='Sue',last_name='Manson',course='Laravel')
# Students.create(adm_no=1438,first_name='Deloris',last_name='Abanathe',course='JavaScript')
# Students.create(adm_no=1298,first_name='Stephen',last_name='Hawking',course='ReactJS')

# After running the code above comment it so as to avoid redundant data then proceed.
"""Looping through data in the table(Select)"""
# select = Students.select()
# for student in select:
#    print('I am {} and I\'m studying {}'.format(student.first_name, student.course))

# After running the code above comment it so as to avoid redundant processing of data then proceed.

"""Fetching a particular data item using criteria"""
# creating a variable that stores the data to be fetched
student = Students.get(id = 5)      # Selects the fifth entry in the table
print('Hi. Im {} and im index five. I study {}.'.format(student.first_name, student.course))

"""Deleting Data from table"""
delete = Students.delete().where(Students.id == 2)
delete.execute()

"""Updating data in the database"""
update = Students.update({Students.course: 'ReactNative'}).where(Students.id == 7)
update.execute()

"""Messin around"""
# counting data items of a particular criteria
countJS = Students.select().where(Students.course == 'JavaScript').count()
print('{} students are taking JavaScript.'.format(countJS))

searchName = input('Enter student\'s first name')
search = Students.select().where(Students.first_name == searchName)
print('Adm No   :   {}\n'
      'Full name:   {}\n'
      'Course   :   {}'
      .format(Students.adm_no, Students.first_name + " " + Students.last_name, Students.course))
