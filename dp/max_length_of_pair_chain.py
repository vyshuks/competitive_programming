# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

# Link: https://leetcode.com/problems/maximum-length-of-pair-chain/


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1] * len(pairs)
        pairs.sort()
        
        i = 1
        j = 0
        while i < len(pairs):
            j = 0
            while j < i:
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
                j+=1
            i+=1
        return max(dp)