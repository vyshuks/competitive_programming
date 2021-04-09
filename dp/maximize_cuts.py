# Given an integer N denoting the Length of a line segment. 
# You need to cut the line segment in such a way that the cut 
# length of a line segment each time is either x , y or z. Here x, y, and z are integers.
# After performing all the cut operations, your total number of cut segments must be maximum.

def maximizeTheCuts(n,x,y,z):
    dp = [-1] * (n+1)
    dp[0] = 0
    
    for i in range(n+1):
        if dp[i] == -1:
            continue
        if (i+x) <= n:
            dp[i+x] = max(dp[i+x], dp[i]+1)
        if (i+y) <= n:
            dp[i+y] = max(dp[i+y], dp[i]+1)
        if (i+z) <= n:
            dp[i+z] = max(dp[i+z], dp[i]+1)
    
    return dp[n] if dp[n] != -1 else 0

expected = 4
assert expected == maximizeTheCuts(4,2,1,1)