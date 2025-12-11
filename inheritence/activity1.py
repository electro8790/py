class vehicle:
    def __init__(self,name,topspeed,mileage):
        self.name= name
        self.topspeed=topspeed
        self.mileage=mileage

class bus(vehicle):
    def __init__(self,name,topspeed,mileage):
        super().__init__(name,topspeed,mileage)
school_bus= bus('school volvo',150,100)
print('name',school_bus.name,'top speed',school_bus.topspeed,'mileage',school_bus.mileage)