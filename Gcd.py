def gcd(m,n):
r=m%n
if(r==0):
   return n
else:
return gcd(n,r)
m=int(input("enter the value"))
n=int(input("enter the value"))
if n>m:
print("  ",gcd(n,m))
else:
print("   ",gcd(m,n))
