def can_sum(targetsum, arr):
    table = [False] * (targetsum+1)
    table[0] = True

    for i in range(targetsum+1):
        if table[i]:
            for num in arr:
                if (i+num) <= targetsum:
                    table[i+num] = True

    return table[targetsum]


# time -> O(mn)
# space -> O(m)
print(can_sum(7, [5,4,3,7]))
print(can_sum(7, [2,4]))
