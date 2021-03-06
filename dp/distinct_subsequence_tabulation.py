def distinct_subsequence(s, t):
    table = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]

    for i in range(len(s)+1):
        table[0][i] = 1
    
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
            if s[j-1] == t[i-1]:
                table[i][j] = table[i][j-1]+table[i-1][j-1]
            else:
                table[i][j] = table[i][j-1]
    return table[len(t)][len(s)]


print(distinct_subsequence("banana", "ban"))