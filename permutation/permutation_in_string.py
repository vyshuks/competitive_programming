# Given two strings s1 and s2, write a function to return true 
# if s2 contains the permutation of s1. In other words, one of 
# the first string's permutations is the substring of the second string.

# https://leetcode.com/problems/permutation-in-string/

def checkInclusion(s1: str, s2: str) -> bool:
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len ==0 or s2_len==0:
        return False
    
    if s2_len > s1_len:
        return False
    
    s2_counter = {}
    s1_counter = {}
    for s in s2:
        s2_counter[s] = s2_counter.get(s, 0) + 1
    # result = 0

    for i,s in enumerate(s1):
        s1_counter[s] = s1_counter.get(s,0) + 1
        if i >= s2_len:
            if s1_counter[s1[i-s2_len]] > 1:
                s1_counter[s1[i-s2_len]] -= 1
            else:
                del s1_counter[s1[i-s2_len]]

        if s1_counter == s2_counter:
            # result += 1
            return True
    return False

print(checkInclusion("eidbaoocbao", "ab"))