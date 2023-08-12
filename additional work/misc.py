#a1=["python","Java", "Ruby", "C++"]
#print(a1)
#b1=[1,2,3]
#print(a1[b1[0]],a1[b1[1]],a1[b1[2]])
#############################
#a1=[1,2,3,4,5,6,7]
#b=[]
#b.append(a1[0])
#b.append(a1[-3:])
#print(b)
###################################



##########################
##L=["Apple","78","970.03"]
#while True:
   # response = input("Enter a number: ")
   # if response == "quit":
      # break
   # else:
        #L.append(response)
#print(L)
######question 1##
courses=["math","science","history"]
print(courses[2])
##length of list##
print(len(courses))
####last element in the list###
print(courses[-1])
#acces first 2 index##
print(courses[0:3])
###last 2 index###
print(courses[1: ])
##add an element to the existing list
courses.append("geography")
print(courses)
###to insert value to given index
courses.insert(0,"art")
print(courses)
courses.insert(1,"social")
print(courses)
###to add multiple value to the list(append only append the second list itself to existing list )
courses_2 = ["humanities","p.Education"]
print(courses_2)
courses.extend(courses_2)
print(courses)
###to remove element from list
courses.remove("math")
print(courses)
####to remove the last value from list
courses.pop()
print(courses)

####to reverse the value in the list
courses.reverse()
print(courses)

#########to sort
courses.sort()
print(courses)
###for sorting number num.sort()


####to find the index##
courses=["math","English","French"]
print(courses.index("math"))
###to chek if element in the list###
print ('math' in courses
       ###list example
number=list(range(20))

#### write a program to print multiplication table for a user given number up to 10####

a=int(input("enter a number: "))

for i in range(10):
    n=a*i
    print(n)
    ###accept age for N number of candidates and print if they are eligible to vote####

k = int(input("enter number of people: "))
age_list=[]
for i in range(k):
        age_list.append(int (input("enter age: ")))
print(age_list)
for n in(age_list):
        if n>=18:
                print(n)
                print("eligible for vote")
        else:
                print(n)
                print("not eligible for vote")

####write a program to chek the number divisible by 2####
k=int(input("enter a value: "))
list_a =[]
for i in range(k):
    list_a.append(int(input("enter number: ")))
    print(list_a)
for n in(list_a):
    if (n%2 ==0):
        print("divisible by 2")
    else:
        print("not divisible by 2 ")
        ########find the length of given value##
k=input("enter a value: ")
m = len(k)
print(m)







