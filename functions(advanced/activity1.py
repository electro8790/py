number1=[1,2,3]
number2=[4,5,6]
result=map(lambda x,y:x+y,number1,number2)
print(list(result))
def square(x):
    return x*x
result1=list(map(square,number1))
print(list(result1))