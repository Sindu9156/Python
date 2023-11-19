 n = int(input())
    arr=[int(arr) for arr in input().split()]
    arr.sort()
    for i in range(1,n):
        if arr[0]!=arr[i]:
            small=arr[i]
            break
    print(small)
