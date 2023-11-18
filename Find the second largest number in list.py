 n = int(input())
    arr=[int(arr) for arr in input().split()]
    big=arr[n-1]
    for i in range(n-2,-1,-1):
        if big!=arr[i]:
            big=arr[i]
            break
    print(big)
