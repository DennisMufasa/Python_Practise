
def largest(x,y,z):
    num=[]
    num.append(x)
    num.append(y)
    num.append(z)

    max=0
    for no in num:

        if no>max:
            max=no

    return max

greatest=largest(1.56,1.056,1.0056)
print("Largest number is ",greatest)