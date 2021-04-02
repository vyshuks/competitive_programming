def can_construct(target_str, arr, memo=None):
    if memo is None:
        memo = {}
    if target_str in memo:
        return memo[target_str]
    if target_str == "":
        return True
    
    for word in arr:
        if target_str.startswith(word):
            result = can_construct(target_str[len(word)::], arr, memo)
            if result:
                memo[target_str] = result
                return True
            
    memo[target_str] = False
    return False


print(can_construct("abcdef", ["abc", "def", "ab"]))
print(can_construct("abcdef", ["abc", "de", "ab"]))
