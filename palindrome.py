def pali(word):
    word=word.replace(' ','')
    word=word.casefold()
    if list(word)==list(reversed(word)):
        return True
    else:
        return False

name=pali('Stanley Yelnats')
print(name)