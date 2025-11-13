dict1={'1':2,'2':2,'3':2,'4':2,'5':1,'6':2,'7':5,'8':1}
print('original dictionary is',dict1)
k=2
q=1
result=0
result1=0
extra=0
for key in dict1:
    if dict1[key]==k:
        result=result+1
    elif dict1[key]==q:
        result1=result1+1
    else:
        extra=extra+1
print('number of 1 is',result)
print('number of 2 is',result1)
print('number of other number is',extra)
