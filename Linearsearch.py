a=[]
n=int(input("enter the value"))

for i in range(0,n):
	a.append(int(input("enter the values")))
s=int(input("enter the value to search"))
for i in range(0,n):
	flag=0
	if(s==a[i]):
		flag=1
		break


if(flag!=1):
	print("the element ",s,"is not found")
else:
	print("the element",s,"is found in position",i)	 
