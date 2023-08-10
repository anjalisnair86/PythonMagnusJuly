

#####question 1######

a=['python','java','ruby','move','c++','go','c','r','swift','pearl']
index_list=[]
n= int(input("Enter a number <=9: "))
for i in range(n):
    index_list.append(int(input("Enter an index: ")))
print(index_list)
print("Requested values from the pre defined list:")
for i in(index_list):
    print(a[i])


########question 2#############

n=int(input("Enter the length of list: "))
new_list=[]
final_list=[]
for i in range(n):
    new_list.append(int(input("Enter a value: ")))
final_list.append(new_list[:3])
final_list.append(new_list[-3:])
print("First and Last three values are:")
print(final_list)



#########question3######
L1=[5,13,20,25]
b=[]
for i in L1:
    if(i%5==0):
        b.append(i)
        print(b)


##########question 4#####
L=["Apple","78","970.03"]
n=int(input("Enter how many values to be added: "))
for i in range(n):
    L.append(int(input("Enter a value:")))
print(" The new list is : ")
print(L)


########Question 5
L=['x','y','z']
L2=[]
n=int(input("Enter repetition: "))
for i in range(n):
    #print(L)
    L2.extend(L)
print(L2)



