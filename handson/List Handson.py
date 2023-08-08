########question 2#############


#a1=[10,20,30,40,50,60]
#b1=[a1[0]]
#b2=a1[3:5]
print(b1)
print(b2)
b1.extend(b2)
print(b1)

#########question3######



L1=[5,13,20,25]
b=[]
for i in L1:
    if(i%5==0):
        b.append(i)
        print(b)


        ##########question 4#####


        L=["Apple","78","970.03"]
while True:
    response = input("Enter a number: ")
    if response == "quit":
       break
    else:
        L.append(response)
print(L)
#####question 1######

a=['python','java','ruby','move','c++','go','c','r','swift','pearl']
print(a)
a1=[1,2,3,4,5,6,7,8,9,10]
print(a1)
d1={1:'python',2:'java',3:'ruby',4:'move',5:'c++',6:'go',7:'c',8:'r',9:'swift',10:'pearl'}
print(d1[1])
print(d1[2])
########Question 5
l1=[7,6,5,4]
n=5
l2=[n*l1]
print(l2)
