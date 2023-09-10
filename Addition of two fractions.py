n1=int(input("enter the first number numerator value"))
d1=int(input("enter the first number denominator value"))
n2=int(input("enter the second number numerator value"))
d2=int(input("enter the second number denominator value"))
n3=n1*d2+n2*d1
d3=d1*d2
i=2
while i<=9:
	if(n3%i==0 and d3%i==0):
		n3=n3/i
		d3=d3/i
		i=i-1
	i=i+1
		

print("the addition of two fraction ",n3," / ",d3)

	
