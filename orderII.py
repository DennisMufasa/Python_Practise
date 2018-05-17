def order(x,y):
    start=x
    stop=y
    counter=start
    count=stop
    goingup=True
    while True:
        if goingup:
            print(counter)
            counter+=1
            if counter==count:
                print(counter)
                goingup=False
                counter=start
        elif goingup==False:
            count-=1
            print(count)

            if counter==count:
                break


order(20,30)