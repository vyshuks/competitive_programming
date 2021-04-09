# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# link: https://leetcode.com/problems/wildcard-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_len = len(p)
        s_len = len(s)
        dp = [[False for _ in range(p_len+1)] for _ in range(s_len+1)]
        
        dp[0][0] = True
        
        for i in range(1, s_len+1):
            dp[i][0] = False
        
        for i in range(1, p_len+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-1]
                
        for i in range(1, s_len+1):
            for j in range(1, p_len+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == '*':
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = False
        
        return dp[s_len][p_len]


