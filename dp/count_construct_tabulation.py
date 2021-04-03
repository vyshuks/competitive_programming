def count_construct(targetstr, arr):
    table = [0] * (len(targetstr)+1)

    table[0] = 1

    for i in range((len(targetstr)+1)):
        if table[i]:
            for word in arr:
                if targetstr.startswith(word):
                    if (i+len(word)) <= (len(targetstr)):
                        table[i+len(word)] += table[i]
    
    return table[len(targetstr)]



print(count_construct("abcdef", ["ab", "cde", "abc", "ef", "f", "cdef"]))