def show(x,y):
    start=x;
    end =y;
    counterA=start
    counterB=end
    goingDown=True;
    while True:
        if goingDown:
            print(counterA)
            counterA+=1
            if counterA==counterB:
                print(counterA)
                goingDown=False
                counterA=start
        elif goingDown==False:
            print(counterB)
            counterB-=1
            if counterA==counterB:
                print(counterB)
                break

show(1,10)