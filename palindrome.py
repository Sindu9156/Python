n=int(input()) 
s=n
sum=1
while(n>0):
  rem=n%10
  n=n/10
  sum=sum*10+n
if(s==sum):
    print("palindrome number")
else:
     print("not a palindrome number")
