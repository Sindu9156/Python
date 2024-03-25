a =[] 
n=int(input("enter the total value")) 
for i in range(0,n):
       a.append(int(input())) 
max = a[0]

for i in range(1,len(a)):
if a[i] > max:
     max = a[i]

print (max)
