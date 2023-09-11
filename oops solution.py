class Car:
    def _init_(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started = False
        self.current_speed = 0
    def start_engine(self):
       self.is_engine_started = True
    def stop_engine(self):
        self.is_engine_started = False
    def accelerate(self):
        if not self.is_engine_started:
            print("car has not yet started")
        else:
            self.current_speed += self.acceleration
            if self.current_speed<0:
                self.current_speed=0
    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")

        else:
            print("car has not started yet")
class Truck:
    def _init_(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super()._init(self,color,max_speed,acceleration,tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self.load=0
    def load_cargo(self,cargo_weight):
        if self.is_engine_started:
            print("cannot unload cargo during motion")
        else:
            self.load= cargo_weight
            if self.load < 0:
                self.load = 0
    def sound_horn(self):
        if self.is_engine_started:
            print("honk,honk")
        else:
            print("car has not started yet")





