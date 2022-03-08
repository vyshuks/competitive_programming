import heapq

nums = [3,2,1,5,6,4]

def find_kth_largest_number(nums, k):
    nums = [-num for num in nums]
    heapq.heapify(nums)
    for _ in range(k-1):
        heapq.heappop(nums)
    return -heapq.heappop(nums)

    

res = find_kth_largest_number(nums, 2)
print(res)


