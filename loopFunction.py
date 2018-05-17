def list(x,y):
    start=x
    stop=y
    counter=start
    count=stop
    while True:
        counter += 1
        print(counter)

        if counter==count:
            count -= 1
            print(count)

            if count==start:
                count-=1
                print(count)
            else:
                break

num=list(0,10)
print(num)

