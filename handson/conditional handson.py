####Question1####
#response_name = input("enter name: ")
#response_marks = input("enter mark: ")
#if int(response_marks) > 50:
    #print("pass")
#else:
    #print("fail")
######question 2#####
response_length = input("enter length: ")
response_width = input("enter width: ")
if int(response_length == response_width):
     print("square")
else:
      print("rectangle")

      ######question 3###
response_Tem= int(input("enter temperature: "))
if 15< response_Tem <40:
    print("Can go for a walk")
else:
    print("can not go for walk")

    #####Question 4#####

response_playerA = int(input("enter score of player A: "))
response_playerB = int(input("enter score of player B: "))

total = response_playerA + response_playerB

if (response_playerA > 300 or response_playerB > 300) and total<500:

response_playerA = int(input("enter score of player A: "))
response_playerB = int(input("enter score of player B: "))

total = response_playerA + response_playerB

if (response_playerA > 300 or response_playerB > 300) and total<500:

    print("can Team up")
else:
    print("can not Team up")
    ######Question 6###


    response_name = input("enter Name: ")
response_salary =int(input("enter Salary: "))
response_experience = int(input("enter years of experience: "))
if response_experience > 5 :
    print("Eligible for 5% Bonus")
else:
    print("Not eligible for bonus")

####Question7####

response_DigitA =input("enter first digit: ")
response_DigitB = input("enter Second digit: ")

N = response_DigitA + response_DigitB
print(N)
if int((response_DigitA + response_DigitB)) ==7:
    print("special number")
elif (response_DigitA == 7) or (response_DigitB == 7):
    print("special number")
elif (int(N)%7==0):
    print("Special number")
else:
    print("Normal number")

    print("can Team up")
else:
    print("can not Team up")

      ######question 5####

response_AngleA=input("enter AngleA: ")
response_AngleB=input("enter AngleB: ")
response_AngleC=input("enter AngleC: ")
if int((response_AngleA+response_AngleB+response_AngleC)==180):
   print("It is a Triangle")
else:
    print("it is not a Triangle")



####question 8
n = input("enter a string: ")
print(n)
k = n[:3]
print(k)
if k == "nxt":
    print("special string")
for i in n[3:]:
    if i.isdigit():
        if(int(i)%2 == 0 or int(i)%7 == 0):
            print("special string")
    else:
        print("not special string")



