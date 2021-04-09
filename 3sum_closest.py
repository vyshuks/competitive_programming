# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        nums.sort()
        
        for i in range(len(nums)-2):
            left_ptr = i + 1
            right_ptr = len(nums)-1
            
            while left_ptr < right_ptr:
                s = nums[i] + nums[left_ptr] + nums[right_ptr]
                if abs(target-s) < abs(target-closest_sum):
                    closest_sum = s
                
                if target < s:
                    right_ptr-=1
                else:
                    left_ptr+=1
        return closest_sum
                    
                