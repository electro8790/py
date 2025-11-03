list1=[]
startnum=int(input('enter starting number'))
endnum=int(input('enter start number'))
for i in range (startnum,endnum):
    if i*i<endnum:
        if i%2==0:
            list1.append(i)
        else:
            continue
    else:
        continue
print("all the even numbers are",list1)        