s1=[1,2,3]
s2=[1,5,6]
s3=list(zip(s1,s2))
print(s3)
for x,y in zip(s1,s2[::-1]):
    print(x,y)
newdicts={s1:s2 for s1,s2 in zip(s1,s2)}
print(newdicts)