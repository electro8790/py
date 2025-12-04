import random
list1=[]
num=int(input('enter length of password'))
for i in range(1,num+1):
    list1.append(random.randint(1,9))
lens=len(list1)
print('you password is')
for i in range(0,lens):
    print(list1[i])
    