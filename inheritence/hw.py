class Vehicle:
    def __init__(self, seatingcapacity):
        self.seatingcapacity =seatingcapacity

    def fare(self):
        return self.seatingcapacity * 100


class Bus(Vehicle):
    def fare(self):
        totalfare =super().fare()+super().fare()*10/100
        return totalfare


bus = Bus(70)
print("Total bus fare is", bus.fare())
    