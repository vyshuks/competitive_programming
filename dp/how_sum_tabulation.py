def how_sum(targetsum, arr):
    table = [None] * (targetsum+1)
    table[0] = []

    for i in range(targetsum+1):
        if table[i] is not None:
            for num in arr:
                result = [*table[i], num]
                if (i+num) <= targetsum:
                    table[i+num]  = result
    
    return table[targetsum]


# time-> O(n*m^2)
# space -> O(m^2)

print(how_sum(7, [5,4,3,7]))
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
print(how_sum(300, [7,14]))