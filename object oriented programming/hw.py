class DOG:
    species='dog'
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age
wuck=DOG('DALMANIAN',5)
buck=DOG('GERMAN SHEPARD',6)
print('buck is a ',buck.species)
print('wuck is a',wuck.species)
print('buck is a',buck.breed,buck.age,'years old')
print('wuck is a',wuck.breed,wuck.age,'years old')