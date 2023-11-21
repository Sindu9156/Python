n=int(input()) 
x=int(input()) 
y=int(input()) 
z=int(input()) 
l1=[] 
    for i in range(0,x+1):
    for j in range(0,y+1):
    for k in range(0,z+1):
         l=[] 
         if i+j+k!=n:
             l.append(i)
            l.append(j)
            l.append(k)
            l1.append(l) 
print(l1) 
