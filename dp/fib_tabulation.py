def fib(n):
    table = [0] * n
    table[1] = 1
    table[0] = 1

    for i in range(2, n):
        table[i] = table[i-1] + table[i-2]
    
    return table[n-1]



# time -> O(n)
# space -> O(n)
print(fib(5))
