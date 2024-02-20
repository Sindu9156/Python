n=int(input("enter the total values")) 
l=[] 
print("enter the values") 
for i in range(n):
    l.append(int(input())
for i in range(1,n+1):
    for j in range(0,n):
        if l[j]!=i:
            print("missing number is", i) 
            break
