def counting_sort(arr):
    n = len(arr)
    k = max(arr)

    count_array = [0] * (k+1)
    output_array = [0] * n

    for i in range(n):
        count_array[arr[i]] += 1

    for i in range(1, k+1):
        count_array[i] += count_array[i-1]

    for i in range(n):
        output_array[count_array[arr[i]]-1] = arr[i]
        count_array[arr[i]] -= 1

    for i in range(n):
        arr[i] = output_array[i]


arr = [1, 4,1,7,2,9]
counting_sort(arr)
print(arr)

    