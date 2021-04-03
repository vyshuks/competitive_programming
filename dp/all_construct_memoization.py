def all_construct(targetstr, arr, memo=None):
    if memo is None:
        memo = {}
    if targetstr in memo:
        return memo[targetstr]
    if targetstr == "":
        return [[]]
    
    combination = []
    for word in arr:
        if targetstr.startswith(word):
            result = all_construct(targetstr[len(word)::], arr)
            for i,r in enumerate(result):
                result[i].append(word)
            
            combination.extend(result)

    memo[targetstr] = combination
    return combination


print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))

