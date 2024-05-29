n= int(input("Enter the Number:"))
temp = n
rev= 0
while n > 0:
    r = n % 10
    rev = (rev * 10) + r
    n= n // 10
print("the reverse of the number is ", rev) 
