class Parrot:
    species='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
woo=Parrot('woo',5)
blu=Parrot('blu',6)
print('blu is a ',blu.species)
print('woo is also a',woo.species)
print('blu is ',blu.name,blu.age)
print('woo is ',woo.name,woo.age)