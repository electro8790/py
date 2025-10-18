try:
    number=int(input('enter a number:'))
    print('the number is ',number)
except ValueError:
    print('exception')