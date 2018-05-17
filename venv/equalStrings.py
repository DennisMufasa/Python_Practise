def equal(x):
    word=x
    word=word.replace(' ','')
    word.casefold()
    length=len(word)
    first=round(length/2)
    sec=length-first
    if first!=sec:
        print("NON-EQUAL HALVES")
    else:
        print("EQUAL HALVES")

equal('Stanley Yelnats')