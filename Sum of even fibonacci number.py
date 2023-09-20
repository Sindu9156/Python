n=int(input("enter the value"))
a=0
b=1
c=a+b
count=0

while(c<n):
	a=b
	b=c
	if(c%2==0):
	  count=count+c
	c=a+b
	
print("  ",count)

