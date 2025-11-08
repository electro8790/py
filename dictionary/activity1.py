dict1={'id1':{'name':'david','class':'V','subject':'maths'},'id2':{'name':'sarah','class':'VI','subject':'english'},'id3':{'name':'John','class':'VI','subject':'science'},'id4':{'name':'sarah','class':'VI','subject':'english'}}
result={}
for key,value in dict1.items():
    if value not in result.values():
        result[key]=value
print(result)