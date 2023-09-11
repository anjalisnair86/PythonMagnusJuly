class Car:


    def __init__(self,color,max_speed,acceleration,tyre_friction,is_engine_started,current_speed):
     self.color=color
     self.max_speed = max_speed
     self.acceleration= acceleration
     self.tyre_friction = tyre_friction
     self.is_engine_started = False

     self.current_speed = 0

class Truck(Car):


    def __init__(self,max_cargo_weight,load,color,max_speed,acceleration,tyre_friction,is_engine_started,current_speed):
      super().__init__(color,max_speed,acceleration,tyre_friction,is_engine_started,current_speed)

obj1 = Truck()
obj1.color()


obj1 = Truck()
obj1.color()

