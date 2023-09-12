class Car:


    def __init__(self,color,max_speed,acceleration,tyre_friction,is_engine_started,current_speed):
        self.color= color
        self.max_speed = max_speed
        self.acceleration= acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = is_engine_started
        self.current_speed = current_speed

class Truck(Car):
    pass

    #def __init__(self,max_cargo_weight,load,color,max_speed,acceleration,tyre_friction,is_engine_started,current_speed):
    #super().__init__(color,max_speed,acceleration,tyre_friction,is_engine_started,current_speed)

obj1 = Truck('Black', 100, 60, 20, True, 80)
print(obj1.color)

