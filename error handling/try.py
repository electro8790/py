try:
    a,b=eval(input('enter two number, seperated by comma'))
    c=(a/b)
    print('the result is',c)
except ZeroDivisionError:
    print('you cannot divide by zero')
except SystemError:
    print('syntax error')
except:
    print('wrong input')
else:
    print('no errors')
finally:
    print('this will run always')