class Vehicle:
    def max_speed(self):
        print(240)
    def mileage(self):
        print(18)
model1x=Vehicle()
model1x.max_speed()

class Bus(Vehicle):
    def seating_capacity(self):
        print(50)

obj1=Bus()
obj1.max_speed()
obj1.seating_capacity()


