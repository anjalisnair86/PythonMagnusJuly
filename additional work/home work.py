class Sample:
    def m1(self):
        a = 10
        b = 0
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Zero division done")

    def m2(self):
        c=10
        try:
            print(d)
        except NameError as e:
            print(e)
        finally:
            print("name error done")

obj = Sample()
obj.m1()
obj.m2()



