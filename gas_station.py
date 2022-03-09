"""
https://leetcode.com/problems/gas-station/
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start = 0
        current = 0
        l = len(gas)
        for i in range(l):
            current += gas[i]-cost[i]
            if current < 0:
                start = i+1
                current = 0
            
        return start