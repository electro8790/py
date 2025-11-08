total=int(input('enter total bill'))
paid=int(input('enter amount you have paid'))
print("you have",total-paid,"amount left to paid")
total=total-paid
for i in range(1,10):
    if total==0:
        print('you have paid the bill in full')
        break
    else:
        paid=int(input('enter amount you have paid'))
        print("you have",total-paid,"amount left to paid")
        total=total-paid