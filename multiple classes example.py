#class Sample:
 #   def m1(self):
       # print("Welcome M1 function")
#class Demo:
    #def m2(self):
       # print("welcome M2 function")

#obj1 = Sample()
#obj2 = Demo()

#obj1.m1()
#obj2.m2()


#########################single inheritance####one Class to other Class#####
#class Sample:
   # def m1(self):
      #  print("Welcome M1 function")

#class Demo(Sample):
    #def m2(self):
      #  print("welcome m2 function")
#obj1=Demo()

#obj1.m1()
#obj1.m2()
########multiple inheritance#######
#class Father:
          #def m1(self):
              #print("car")
#class Mother:
     #def m2(self):
         #print("House")
#class Son(Father,Mother):
    #def m3(self):
        #print()
#obj1=Son()
#obj1.m1()
#obj1.m2()
#####multy layer inheritance####
class Father:
    def m1(self):
        print("car")
class Mother(Father):
    def m2(self):
        print("house")
class Son(Mother):
    def m3(self):
            print()
obj1=Son()
obj1.m1()
obj1.m2()
obj1.m3()
