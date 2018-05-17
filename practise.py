data="I am the only one with the qualification for this job."
newData=data.strip()
length=len(newData)
print(length)


word='dennis'
length=len(word)
first=round(length/2)
sec=length-first
if first!=sec:
    print("FALSE")
else:
    print("TRUE")

name='Mufasam'
newName=name.lower()
newName=newName.count('m')
print(newName)

word='fool'
o=word.find('ol')
print(o)