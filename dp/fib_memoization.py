def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# 0 1 1 2 3 5
# time -> O(n)
# space -> O(n)

print(fib(5))
print(fib(50))