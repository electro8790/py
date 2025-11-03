vowels=0
consonents=0
uppercase=0
lower=0
alphabets=0
digits=0
for i in range(1,21,1):
    c=input('enter character')
    if c== 'a' or 'e' or 'i' or 'u' or 'o':
        alphabets=alphabets+1
        vowels=vowels+1
        if c.isupper():
            uppercase=uppercase+1
        else:
            lower=lower+1
    elif c.isdigit:
        digits=digits+1
    else:
        consonents=consonents+1
        if c.isupper:
            uppercase=uppercase+1
        else:
            lower=lower+1
print('you have',alphabets,'alphabets and',digits,'digits and',lower,'lower case alphabets nad',uppercase,'upper casre alphabets and',vowels,'vowels',consonents,'consonents')
        