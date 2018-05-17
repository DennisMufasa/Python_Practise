# counting number of times a character appears in a string
word="Josephine"
count=0
for letter in word:
    if letter=="e":
        count+=1
print(count)

def charCounter(x,y):
    name=x
    char=y

    counter=0
    for i in name:
        if i==char:
            counter+=1
    print(counter)

charCounter("Dennis","n")

