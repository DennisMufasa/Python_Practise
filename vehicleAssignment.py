from peewee import  *
db=SqliteDatabase("Magari.db")

class vehicles(Model):
    plate=CharField(unique=True)
    make=TextField()
    model=CharField()
    year=IntegerField()
    RHD=BooleanField()
    price=FloatField()
    colour=TextField()
    dateOfMan=DateField(formats=['%Y-%m-%d'])

    class Meta:
        database=db

# vehicles.create_table()

# vehicles.create(plate='KAZ',make='Toyota',model='Fortuner',year=2008,RHD=True,price=60000,colour='Red',dateOfMan='2008-10-5')
# vehicles.create(plate='KBD',make='Range',model='Sports',year=2012,RHD=True,price=75000,colour='Silver',dateOfMan='2012-5-10')
# vehicles.create(plate='KCE',make='Subaru',model='Forester',year=2010,RHD=False,price=12000,colour='Black',dateOfMan='2010-11-8')
# vehicles.create(plate='KZX',make='Nissan',model='GTR',year=2006,RHD=False,price=55000,colour='Grey',dateOfMan='2005-12-6')
# vehicles.create(plate='KAB',make='Audi',model='R8',year=2007,RHD=True,price=85000,colour='Blue',dateOfMan='2007-1-7')
# vehicles.create(plate='KAC',make='Toyota',model='supra',year=2009,RHD=False,price=65000,colour='Platinum',dateOfMan='2009-5-12')

# select=vehicles.select()
# for v in select:
#     print(v.make,v.model,v.plate,v.year,v.price,v.colour,v.dateOfMan)
#
# make=vehicles.get(id=5)
# print(make.make,make.model,make.plate,make.year,'RHD-',make.RHD,make.colour,'cost USD-',make.price)
#
# make=vehicles.select().where(vehicles.make=='Toyota')
# for i in make:
#     print(i.make,i.model,i.plate,i.year,i.colour)
#
# delete=vehicles.delete().where(vehicles.id==4)
# delete.execute()
#
# update=vehicles.update({vehicles.price:80000}).where(vehicles.id==1)
# update.execute()

# count=vehicles.select().where(vehicles.make=='Toyota').count()
# print(count)

