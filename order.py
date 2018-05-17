def list(x,y):
    start=x
    stop=y
    counter=start
    count=stop
    goingup=True
    while True:
        if goingup:
            print(counter)
            counter += 1
            if counter==count:
                print(counter)
                goingup=False



list(10,30)