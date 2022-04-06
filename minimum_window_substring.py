from collections import Counter

def min_window_substring(s, t):

    S = len(s)
    T = len(t)
    if T > S or t=="":
        return ""
    start , end = 0, S
    t_counter = Counter(t)
    s_counter = Counter()
    left = 0
    right = 0
    required = len(t_counter)
    satisfied = 0
    for right in range(S):
        s_counter[s[right]] +=1
        if s[right] in t_counter and t_counter[s[right]] == s_counter[s[right]]:
            satisfied +=1
        if satisfied == required:
            while s[left] not in t_counter or s_counter[s[left]] >  t_counter[s[left]]:
                s_counter[s[left]] -=1
                left += 1
            if right-left+1 < end-start+1:
                start,end = left, right



    
    return s[start: end+1] if end-start+1 <=S else ""

def main():
    s = "A"
    t = "B"
    print(min_window_substring(s,t))

main()