from typing import List


def maxProfit(prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*l for _ in range(3)]
        max_dif = -prices[0]
        for i in range(1, 3):
            for j in range(1, l):
                max_dif = max(max_dif, dp[i-1][j] - prices[j])
                dp[i][j] = max(dp[i][j-1], prices[j]+max_dif)
        return dp[2][l-1]

print(maxProfit([2,4,8,6,7]))
print(maxProfit([3,3,5,0,0,3,1,4]))
# for o to j
# x1 = dp[i][j] - dp[i][j-1]
# x2 = dp[i][j] - dp[i][j-2]
