def GCD(num1, num2):
    if num1 > num2:
        r= num2
    else:
        r = num1
    for i in range(1, r+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print(gcd)

n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
GCD(n1, n2) 
