class Car2022:
    def roof(self):
        print("Normal roof")
    def wheel(self):
        print("Normal roof")
    def music(self):
        print("12 inch screen")
class Car2023(Car2022):
    def roof(self):
       # print("sun roof")
        super().roof()
    def wheel(self):
        print("alloy wheel")
    def music(self):
        print("16 inch screen")


obj1 = Car2023()
obj1.roof()
obj1.music()

