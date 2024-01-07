N = int(input())
arr1 = [0] * 3
arr2 = [0] * 3
for _ in range(N):
    a, b, c = map(int, input().strip().split())
    
    arr1[0] += a
    arr1[1] += b
    arr1[2] += c
    arr2[0] += a*a
    arr2[1] += b*b
    arr2[2] += c*c

max_value = max(arr1)
if arr1.count(max_value) == 1:
    for i in range(3):
        if arr1[i] == max_value:
            print(i+1, max_value)
else: 
    next_max_value = max(arr2)
    idx = arr2.index(next_max_value)
    if arr2.count(next_max_value) == 1:
        print(idx+1, arr1[idx])
    else:
        print(0, arr1[idx])