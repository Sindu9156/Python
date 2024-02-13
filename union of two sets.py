s1=set()
s2=set()
n=int(input("enter the total values for s1 and s2"))
print("enter values for set 1")
for i in range(0,n):
    s1.add(int(input()))

print("enter values for set 1")
for i in range(0,n):
    s2.add(int(input()))


print("union of s1 and s2 is",s1.union(s2))
