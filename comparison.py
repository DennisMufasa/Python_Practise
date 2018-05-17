
word='banana'
if word=='banana':
    print('All rigth, bananas.')

def comp(a):
    word=a
    if word=='banana':
        print('All right banana')

comp("banana")

def comparisom(b):
    word=b
    word.lower()
    if word>'banana':
        print('Your word', word,' is bigger than banana')
    elif word<'banana':
        print('Your word', word,' smaller than banana.')
    else:
        print('All right bananas.')

comparisom('Apple')
comparisom('oranges')
comparisom('Pussy')
