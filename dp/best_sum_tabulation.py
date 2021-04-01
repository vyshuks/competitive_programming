def best_sum(targetsum, arr):
    table = [None] * (targetsum+1)
    table[0] = []

    for i in range(targetsum+1):
        if table[i] is not None:
            for num in arr:
                if (num+i) <= targetsum:
                    combination = [*table[i], num]
                    if table[num+i] is None or len(combination) < len(table[num+i]):
                        table[num+i] = combination

    return table[targetsum]


# time-> O(n*m^2)
# space -> O(m^2)
print(best_sum(7, [5,3,4,7]))
print(best_sum(8, [5,3,2]))
print(best_sum(100, [1,2,5,25]))