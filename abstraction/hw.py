class BMW:
    def fuel_type(self,type):
        print('the fuel type is',type)
    def topspeed(self,speed):
        print('the top speed is',speed)
class Ferrari(BMW):
    def fuel_type(self,type):
        print('the fuel type is',type)
    def topspeed(self,speed):
        print('the top speed is',speed)    
car1=Ferrari()
car1.fuel_type('racing')
car1.topspeed(200)
car2=BMW()
car2.fuel_type('premium')
car2.topspeed(180)