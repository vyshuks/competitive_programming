def counting_sort(arr, exp):
    n = len(arr)
    output_array  = [0] * n
    count_array = [0] * 10

    for i in range(n):
        index = (arr[i] / exp)
        count_array[int(index%10)] += 1
    
    for i in range(1,10):
        count_array[i] = count_array[i] + count_array[i-1]

    for i in range(n-1,-1,-1):
        index = (arr[i] / exp)
        output_array[count_array[int(index%10)]-1] = arr[i]
        count_array[int(index%10)]-=1

    for i in range(n):
        arr[i] = output_array[i]



def radix_sort(arr):
    
    max_num = max(arr)

    
    exp = 1
    while max_num/exp > 0:
        counting_sort(arr, exp)
        exp*=10

arr = [1, 4,1,7,2,9]
radix_sort(arr)
print(arr)
