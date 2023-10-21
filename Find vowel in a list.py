a=[]
n=int(input("Enter the total elements"))
for i in range(0,n):
    b=input("Enter")
    a.append(b)
i=0
while(i<n):
    if(a[i]=='a'):
        print("vowel") 
    elif(a[i]=='e'):
        print("vowel")
    elif(a[i]=='i'):
        print("vowel")
    elif(a[i]=='o'):
        print("vowel")
    else:
        print("consonant")
    i=i+1         
