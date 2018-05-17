def bmi(w,h):
    bmi=(w/(h*h))
    return bmi

myBmi=bmi(70,1.85)
print(myBmi)

def max(x,y):
    largest=0
    for i in range(x,y):
        if i>largest:
            largest=i
    return largest

greatest=max(10,30)
print(greatest)