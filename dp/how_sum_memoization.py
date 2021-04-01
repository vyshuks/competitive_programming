def how_sum(targetsum, arr, memo=None):
    if memo is None:
        memo = {}
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    
    
    for num in arr:
        remainder = targetsum-num
        result = how_sum(remainder, arr, memo)
        if result is not None:
            result = [*result, num]
            memo[targetsum] = result
            return result
    
    memo[targetsum] = None    
    return None


# time-> O(n*m^2)
# space -> O(m^2)
print(how_sum(7, [5,4,3,7]))
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
print(how_sum(300, [7,14]))
