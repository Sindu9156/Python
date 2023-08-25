list=[]
n=int(input("enter the total value"))
for i in range(0,n):
	a=int(input("enter the values"))
	list.append(a)
print("type",type(list))
print(list)
list1=list.copy()
print("copy of the list",list1)
