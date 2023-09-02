def gcd(a,b):
	r=(a%b)
	if r>0:
		b=gcd(b,r)
	return b


a=int(input("enter the value"))
b=int(input("enter the value"))
if a<b:
	c=a
	a=b
	b=c
	
print("gcd of ",a,"and",b,"is",gcd(a,b))
