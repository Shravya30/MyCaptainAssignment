list=[]
n=int(input("number of elements to enter to list:"))
for i in range(0,n):
    num=int(input())
    list.extend([num])
print("list:",list)
i=0
list1=[]
for i in range(len(list)):
    if list[i]>0:
        list1.extend([list[i]])
print("positive number range:",list1)

