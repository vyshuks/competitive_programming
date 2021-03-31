def grid_travel(rows, cols, memo={}):
    if (rows, cols) in memo:
        return memo[(rows, cols)]
    if rows == 0 or cols == 0:
        return 0
    if rows == 1 and cols == 1:
        return 1
    result = grid_travel(rows-1, cols) + grid_travel(rows, cols-1)
    memo[(rows, cols)] = result
    return memo[(rows, cols)]



# time -> O(m+n)
# space -> O(m+n)
print(grid_travel(2, 3))
print(grid_travel(3, 3))
print(grid_travel(18, 18))