class IOSTRING():
    def __init__(self):
        self.str1=''
    def gettingstring(self):
        self.str1= input('enter a string')
    def printuppercase(self):
        print('result is',self.str1.upper())
str1=IOSTRING()
str1.gettingstring()
str1.printuppercase()
