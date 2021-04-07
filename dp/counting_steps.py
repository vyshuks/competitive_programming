# A frog jumps either 1, 2, or 3 steps to go to the top. 
# In how many ways can it reach the top. As the answer 
# will be large find the answer modulo 1000000007.

def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    # code here
    if n==1 or n==0:
        return 1
    table = [0 for _ in range(n+1)]
    table[0] = 1
    table[1] = 1
    table[2] = 2
    
    for i in range(3, n+1):
        # n= 3
        # table[3] = table[2] + table[1] + table[0] -> 4
        # 1+1+1
        # 1+2
        # 2+1
        # 3
        
        # n=4
        #table[4] = table[3] + table[2] + table[1] -> 4 + 2 + 1 -> 7
        table[i] = table[i-1] + table[i-2] + table[i-3]
    return table[n]
