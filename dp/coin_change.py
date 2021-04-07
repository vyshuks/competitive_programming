# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# Link: https://leetcode.com/problems/coin-change/


# tabulation
from typing import List
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount+1 for _ in range(amount+1)]
    # if zero amount then there is 0 coins
    dp[0] = 0 # base condition


    for amt in range(amount+1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], 1+dp[amt-coin])
    return dp[amount] if dp[amount] < amount+1 else -1
    


# memoization

def coinChange(self, coins: List[int], amount: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    
    if amount == 0:
        return 0
    
    
    min =sys.maxsize
    for coin in coins:
        if coin <= amount:
            res = self.coinChange(coins, amount-coin, memo)
            if res < min:
                min=res
    if min != sys.maxsize:
        min = min+1
    else:
        if not memo:
            min = -1
        else:
            min = sys.maxsize
    memo[amount] = min
    return min
        