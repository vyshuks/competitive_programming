def distinct_subsequence(s, t, memo=None):
    if memo is None:
        memo={}
    if (s,t) in memo:
        return memo[(s,t)]
    if len(t) == 0:
        return 1
    if len(s) < len(t):
        return 0
    if s[-1] != t[-1]:
        memo[(s, t)] = distinct_subsequence(s[:-1], t, memo)
        return memo[(s, t)]
    else:
        memo[(s, t)] = distinct_subsequence(s[:-1], t, memo) + distinct_subsequence(s[:-1], t[:-1], memo)
        return memo[(s, t)]


print(distinct_subsequence("banana", "ban"))
print(distinct_subsequence("geeksforgeeks", "ge"))
