n=int(input()) 
sum=0
while(n>0):
  rem=n%10
  sum=sum+rem
  n=n/10;
print("sum of digit of a number is", sum) 
