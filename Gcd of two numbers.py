n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))


def gcd(n1, n2):
    if n1 > n2:
        s= n2
    else:
        s = n1
    for i in range(1, s+1):
        if (n1 % i == 0) and (n2 % i == 0):
            gcd = i
    print("GCD of two Number: ",gcd))

gcd(n1, n2)
