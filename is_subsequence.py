def is_subsequence(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    s2_ptr = 0

    for i in range(s1_len):
        if s1[i] == s2[s2_ptr]:
            s2_ptr+=1
        if s2_ptr == s2_len:
            return True
    if s2_ptr == s2_len:
        return True
    return False


print(is_subsequence("ahbgdc", "abc"))