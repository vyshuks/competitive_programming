# You are given coins of different denominations and a total amount of money.
#  Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.

# Link: https://leetcode.com/problems/coin-change-2/

from typing import List
def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount+1)
    dp[0] = 1

    for coin in coins:
        for amt in range(amount+1):
            if coin <= amt:
                dp[amt] += dp[amt-coin]


    return dp[amount]


expected= 4
res = change(5, [1,2,5])
assert expected == res