t=("hello","welcome","to","GCE")


print(type(t))
print(len(t))
print(t[0])
print(t[-1])
print(t[:])
print(t[1:])
print(t[:2])
print(t[-4:0])
if "hello" in t:
   print("match")
t1=("social","maths","eng","tamil")
print(t1.count("eng"))
print(t1.index("tamil"))
print(t+t1)
(g,a,*b)=t1
print(g)
print(a)
print(b)
