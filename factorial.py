def fact(n):
    if n==0:
        return 1
    else:
        return n* fact(n-1)
number=int(input('Enter the number of your choice'))
result=fact(number)
print('the factorial of the number is' ,result)
