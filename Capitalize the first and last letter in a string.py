a=input("enter the string")
c=len(a)
a=a.replace(a[0],
a[0].upper())
a=a.replace(a[c-1],a[c-1].upper())
print(a)
