n=int(input("enter the value"))
sum=0
for i in range(2,n+1):
	flag=0
	for j in range(2,9):
		if i%j==0 and i!=j:
			flag=1
	if(flag==0):
		sum=sum+i
print("the sum of prime factor is  ",sum)

