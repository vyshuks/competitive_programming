def count_construct(targetstr, arr, memo=None):
    if memo is None:
        memo = {}
    if targetstr in memo:
        return memo[targetstr]

    if targetstr=="":
        return 1

    count = 0
    for word in arr:
        if targetstr.startswith(word):
            count += count_construct(targetstr[len(word)::], arr)
    memo[targetstr] = count
    return count


print(count_construct("abcdef", ["ab", "cde", "abc", "ef", "f", "cdef"]))
    
