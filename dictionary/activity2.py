dict1={'codingle':2,'is':2,'best':2,'for':2,'coding':1}
print('original dictionary is',dict1)
k=2
res=0
for key in dict1:
    if dict1[key]==k:
        res=res+1
print(res)