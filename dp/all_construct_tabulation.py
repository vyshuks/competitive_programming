def all_construct(targetstr, arr):
    table = [None] * (len(targetstr)+1)
    table[0] = [[]]

    for i in range(len(targetstr)+1):
        if type(table[i]) is list:
            for word in arr:
                prefix = targetstr[i: i+len(word)]
                if prefix == word:
                    new_combination = []
                    for _i, r in enumerate(table[i]):
                        new_combination.append([*r,word])
                    
                    if ((i+len(word)) <= len(targetstr)):
                        if table[i+len(word)] is None:
                            table[i+len(word)] = []

                    table[i+len(word)].extend(new_combination)
    
    
    return table[len(targetstr)]


print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))