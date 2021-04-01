def best_sum(targetsum, arr, memo=None):
    if memo is None:
        memo = {}

    if targetsum in memo:
        return memo[targetsum]

    if targetsum == 0:
        return []
    
    if targetsum < 0:
        return None

    shortest_combination = None

    for num in arr:
        remainder = targetsum - num
        result = best_sum(remainder, arr, memo)
        if result is not None:
            combination = [*result, num]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination
                memo[targetsum] = shortest_combination

    memo[targetsum] = shortest_combination
    return shortest_combination


# time-> O(n*m^2)
# space -> O(m^2)
print(best_sum(7, [5,3,4,7]))
print(best_sum(8, [5,3,2]))
print(best_sum(100, [1,2,5,25]))
            