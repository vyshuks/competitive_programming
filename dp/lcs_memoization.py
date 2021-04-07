def lcs(text1, text2, memo=None):
    if memo is None:
        memo = {}
    if (text1, text2) in memo:
        return memo[(text1, text2)]
    if len(text1) == 0 or len(text2) == 0:
        memo[(text1, text2)] = 0
        return 0

    if text1[-1] == text2[-1]:
        memo[(text1, text2)] = 1+ lcs(text1[:-1], text2[:-1], memo)
        return memo[(text1, text2)]
    
    memo[(text1, text2)] = max(lcs(text1[:-1], text2, memo), lcs(text1, text2[:-1], memo))
    return memo[(text1, text2)]


print(lcs("abcde", "ace"))