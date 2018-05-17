# all prime numbers between 2 and 10
for i in range(2, 10):
    if all(i % p for p in range(2, i)):
        print(i)

# all prime numbers between 10 and 100
for j in range(10, 100):
    if all(j % l for l in range(2, j)):
        print(j)
