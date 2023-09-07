def fact(n):
if n==1:
return 1
else:
return n*fact(n-1)

a=int(input("enter the value"))
sum=0
b=a
while(a>0):
r=int(a%10)
sum+=fact(r)
a=int(a/10)
if sum==b:
    print(sum," is a strong number")
else:
print(sum," is not a strong number")
