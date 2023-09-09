b=int(input("enter the binary value"))
i=0
dec=0
while b>0:
	r=int(b%10)
	dec+=r*(pow(2,i))
	i=i+1
	b=int(b/10)
	
print("the decimal value is ",dec)
