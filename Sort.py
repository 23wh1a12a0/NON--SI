a = list(map(int, input().split()))
n = len(a)


for i in range(n):
    min_index = i  # assume current i is the minimum
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    
    a[i], a[min_index] = a[min_index], a[i]

print(a)
