class Mufasa:
    def __init__(self,name,age,profession,health):
        self.name=name
        self.age=age
        self.profession=profession
        self.health=health

    def career(self):
        if  self.profession=='Developer':
            print(self.name,' is a developer.')
        else:
            print(self.name,' is not qualified for this job.')




# wewe=Mufasa('Vicky',23,'IT','Insured')
# wewe.career()

# mimi=Mufasa('Dennis',23,'Developer','Insured')
# mimi.career()
# mimi=Mufasa('Dennis',23,'developer','insured')
# mimi.details('Dennis',23,'developer')
# mimi.job('Anthony','doctor')
# mimi.miaka('Vicky',23)
# mimi.afya('Walter','not insured')