def Sum(n):
  if n == 1:
    return 1
  return num + Sum(num-1)

n=int(input("enter the value")) 
print(Sum(n))
