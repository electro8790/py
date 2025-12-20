class myclass():
    __privatevar=27;
    def __privMeth(self):
        print('I am inside my class')
    def hello(self):
        print('private value',myclass.__privatevar)

X=myclass()
X.hello
X.__privMeth()
