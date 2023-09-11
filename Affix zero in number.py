n=int(input("enter the starting value"))
m=int(input("enter the ending value"))

for i in range(n,m):
	if i>=100:
		print("{:04d}".format(i))
	elif i>=10:
		print("{:03d}".format(i))
	else:
		print("{:02d}".format(i))
		
print(m)
