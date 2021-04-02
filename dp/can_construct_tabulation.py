def can_construct(target_str, arr):
    table = [False] * (len(target_str)+1)
    table[0] = True

    for i in range(len(target_str)+1):
        if table[i]:
            for word in arr:
                prefix = target_str[i: i+len(word)]
                # print(prefix, word)
                if prefix == word:
                    table[i+len(word)] = True
    # print(table)
    return table[len(target_str)]



print(can_construct("abcdef", ["abc", "def", "ab"]))
print(can_construct("abcdef", ["abc", "de", "ab"]))