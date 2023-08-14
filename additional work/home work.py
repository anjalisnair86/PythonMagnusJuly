
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
















