r=int(input("enter the number  row "))
c=int(input("enter the number  column"))
a=[]
for i in range(0,r):
d=[]
for h in range(0,c):
d.append(int(input("enter the value")))
a.append(d)

r1=int(input("enter the number  row "))
c1=int(input("enter the number  column"))
b=[]
for i in range(0,r1):
d=[]
for h in range(0,c1):
d.append(int(input("enter the value")))
b.append(d)

if(c!=r1):
print("multiplication not possible")
else:
e=[]
for i in range(0,r):
d=[]
for j in range(0,c1):
s=0
for k in range(0,r1):
s+=a[i][k]*b[k][j]
d.append(s)
e.append(d)
for i in range(0,r):
for h in range(0,c1):
print(e[i][h],end=" ")
print("\n")
