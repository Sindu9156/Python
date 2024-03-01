s1=set() 
s2=set() 
n=int(input("enter the total value for set1")) 
print("enter the elements for set 1") 
for i in range(n):
    s1.add(int(input())) 
n=int(input("enter the total value for set 2"))
print("enter the elements for set 1") 
for i in range(n):
    s1.add(int(input())) 
print("the difference of two set is", s1.difference_update(s2))
