print("Even numbers")
for i in range(0,11):
    if i%2==0:
        print(i)

print("odd numbers")

for j in range(0,11):
    if j%2!=0:
        print(j)
print("prime numbers")

primes=[]
for k in range(2,100):
    if all(k%p for p in primes):
        print(k)

        primes.append(k)
