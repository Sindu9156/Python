num=int(input("enter the value")) 
num1 = num
sum = 0
l=len(str(num))
for i in range(l):
  r = num%10
  num = num/10
  sum += pow(r,l)
if sum==num1:
  print("Armstrong")
else:
  print("Not Armstrong")
