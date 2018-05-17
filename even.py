# print("even numbers")
# for i in range(1,101):
#     if i%2!=0:
#          print(i)

def evenNo(x,y):
    for i in range(x,y):
        i+=1
        if i%2==0:
            num=i
            print(num)


number=evenNo(0,11)
print(number)