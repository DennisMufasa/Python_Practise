class Emmobilis:

    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
        self.wanafunzi=[]

    def admission(self):

        stdName=self.name
        stdAge=self.age
        stdCourse=self.course
        stdGrade=self.grade
        self.wanafunzi.append({'name':stdName,'age':stdAge,'course':stdCourse,'grade':stdGrade})
        print(self.wanafunzi)

    def allocation(self):

        if self.grade !='A':
            print(self.name,' does not qualify for a scholarship.')
        else:
            print(self.name,' you are qualified for a scholarship.')

    def classList(self):
        print(self.wanafunzi['name'],self.wanafunzi['course'])



std1=Emmobilis('Dennis',23,'Pythone','A')
std1.admission()
std1.allocation()
std2=Emmobilis('Vicky',23,'IT','B')
std2.admission()
std2.allocation()

