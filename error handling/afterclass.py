try:
    age=int(input('enter a number:'))
    if age%2 == 0:
        print('your age is even numeber')
    else:
        print('your age is odd number')
except ValueError:
    print('incorrect value given')