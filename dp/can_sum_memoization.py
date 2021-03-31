def can_sum(targetsum, arr, memo=None):
    if memo is None:
        memo = {}
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return True 
    if targetsum < 0:
        return False

    for num in arr:
        remainder = targetsum-num 
        if can_sum(remainder, arr, memo):
            memo[targetsum] = True
            return True
    
    memo[targetsum] = False
    return False


# time -> O(mn)
# space -> O(m)

print(can_sum(7, [5,3,4,7]))
print(can_sum(7, [2,4]))
print(can_sum(300, [7,14]))