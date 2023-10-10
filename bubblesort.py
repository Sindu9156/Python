n = int(input())

a = list(map(int, input().split()))
swap=0
for j in range(0,n):
    swap1=0
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
            swap=swap+1
            swap1=swap1+1
    if swap1==0:
        break
        
print("Array is sorted in",swap,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])
            
        
