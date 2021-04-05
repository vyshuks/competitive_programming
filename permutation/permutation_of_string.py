def permute(left, right, string):
    
    if left == right:
        print("".join(string))
    else:
        for i in range(left, right+1):
            string[left], string[i] = string[i], string[left]
            permute(left+1, right, string)
            string[left], string[i] = string[i], string[left] # backtrack





def permutation(string):
    l = len(string)
    if l == 1:
        return string
    left = 0
    right = l-1
    permute(left, right, list(string))


permutation("abc")