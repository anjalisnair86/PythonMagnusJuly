########question 2#############
#a1=[10,20,30,40,50,60]
#b1=[a1[0],a1[3:6]]
#print(b1)
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