v=False
while not v:
    try:
        num=int(input('enter a number'))
        while num%2==0:
            print('bye')
        v=True
    except ValueError:
        print('Invalid')
        