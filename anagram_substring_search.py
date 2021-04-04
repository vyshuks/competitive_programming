from collections import defaultdict

def compare(d1,d2):
    for key, val in d1.items():
        if d2.get(key) != val:
            return False
    return True

def search(pattern, text):
    count_of_pattern = defaultdict(int)
    count_of_text = defaultdict(int)

    M = len(pattern)
    N = len(text)
    result = 0
    for i in range(M):
        count_of_pattern[pattern[i]] += 1
        count_of_text[text[i]] += 1

    for i in range(M,N):
        if compare(count_of_pattern, count_of_text):
            result += 1
        
        count_of_text[text[i]] += 1
        count_of_text[text[i-M]] -= 1

    if compare(count_of_pattern, count_of_text):
        result += 1
    
    return result


print(search("ABCD", "BACDGABCDA"))
print(search("AABA", "AAABABAA"))
print(search("abc", "abdcabc"))
        
