n=int(input("enter number of fibanocci numbers to be printed:"))
a=0
b=1
list=[0,1]

for i in range(2,n):
    c=a
    a=b
    b=a+c
    list.extend([b])
print(list)