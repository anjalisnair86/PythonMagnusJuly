###bmi calculator###

#name="patrik"
#weight_kg=70
#height_m=2

#bmi=bmi=weight_kg/(height_m**2)
#print("bmi: ")
#print(bmi)

#if bmi<25:
   # print(name)
   # print
#else:
    #print(name)


response_name=input("enter name: ")
response_weight=input("enter weight: ")
response_height=input("height: ")
bmi=int(response_weight)/(int(response_height)**2)
print("bmi: ")
print(bmi)
if bmi<25:
    print(response_name)
    print("is not over weight")
else:
    print("is over weight")

