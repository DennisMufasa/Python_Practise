word='dennis'
print(type(word))
print(dir(word))

# converting string to uppercase
print(word.upper())

# find out the position a character appears
print(word.find('e'))
print(word.find('nn'))
print(word.find('i',2))

# removing whtespaces before and after string
line=' Here we go '
print(line)
newLine=line.strip()
print(newLine)
# removing whitespaces in between strings
newerLine=line.replace(' ','')
print(newerLine)

# starts with

sentence='Please go home.'
newSent=sentence.lower().startswith('p')
print(newSent)

