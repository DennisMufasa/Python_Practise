
def prime(x, y):
    for i in range(x, y):
        if all(i % p for p in range(2, i)):
            num = i
            print(num)


prime(2, 100)
