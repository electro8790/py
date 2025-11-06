def palindr(r):
    s=len(r)-1
    e=0
    while(s<e):
        if (r[s]!=r[e]):
            return False
        s=s+1
        e=e-1
    return True
tuple1=(1,2,3,3,2,1)
if palindr(tuple1):
    print('it is flip flop')
else:
    print('it is not flip flop')
