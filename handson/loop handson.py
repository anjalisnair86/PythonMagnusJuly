#####question 3

m = int(input("Enter number of rows:"))
n = int(input("Enter number of columns:"))
for i in range(m):
    print(n*'#')

    ###Question1
m = int(input("enter a number: "))
n = int(input("enter a number: "))
k=[]
for i in range(m,n+1):
    k.append(i)
print(k)
####Question 2

n=(int(input("enter a number: ")))
k=[]
for i in range(1,n+1):
    k.append(i)
average=sum(k)/len(k)
print(average)
####question 5

n = (int(input("enter a number: ")))
k = []
for i in range(n+1):
     k.append(i)
print(k)
print(sum(k))



###Question 4###

m=int(input("enter a number: "))
n=int(input("enter a number: "))
for i in range(m):
    print(i)
for j in range(n):
    print(i)


 #####question6
    n = int(input("Enter a number:"))

for j in range(2):
    for i in range(n+1):
            p = str(i)
            print(i*p)
####Question 7#####
n=int(input("enter a number "))
j=[]
for i in range(1,n+1):
  k=i**2
  j.append(k)
  print(sum(j))



