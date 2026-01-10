class stringreverse:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_string(self):
        return self.input_string[::-1]
str='hello,bye'
obj=stringreverse(str)
result=obj.reverse_string()
print(result)