# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#Link: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        j =0
        i =1
        while i <len(nums):
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                j += 1
            i+=1
            
        return max(dp)