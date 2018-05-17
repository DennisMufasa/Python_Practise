from math import  sqrt,pow,pi
def area(a):
    area=(sqrt(3)/4)*a*a
    return area

side=input("enter one side of equilateral Triangle")
side=int(side)

Area=area(side)
print("Area of your Triangle is",Area)


