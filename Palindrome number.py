a=int(input("enter the value"))
n=0
b=a
while(a>0):
r=int(a%10)
n=n*10+r
a=int(a/10)

if(n==b):
print(n,"is a palindrome number")
else:
print(" ",n,"is not a palindrome number")
