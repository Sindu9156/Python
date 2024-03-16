num = int(input("Enter the Number:"))
n,m= 0, 1
print("Fibonacci Series:", n, m, end=" ")
for i in range(2, num):
    n3 = n + m
    n  = m
    m = n3
    print(n3, end=" ")

print()
