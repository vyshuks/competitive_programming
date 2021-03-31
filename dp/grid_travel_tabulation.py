def grid_travel(rows, cols):
    table = [[0] * (rows+1) for _ in range(cols+1)]

    table[1][1] = 1

    for i in range(rows+1):
        for j in range(cols+1):
            current = table[i][j]
            if i+1 <= rows: 
                table[i+1][j] += current
            if j+1 <= cols: 
                table[i][j+1] += current
    
    return table[rows][cols]


# time -> O(mn)
# space -> O(mn)

print(grid_travel(3,3))
print(grid_travel(18, 18))

