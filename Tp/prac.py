n = 4 
m = 4
grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
new_grid = [[0 for _ in range(n)] for _ in range(m)]
row , col = 0 , 0
now = 0
while now <= m // 2:
    for j in range(col, m - col -1):
        new_grid[col][j] = grid[col][j+1]
        row = j
    print(row)
    for i in range(row+1):
        new_grid[i][row+1] = grid[i+1][row+1]
        col = i
    print(new_grid)
    for j in range(col + 1  , m - col -2, -1):
        new_grid[col+1][j] = grid[col+1][j - 1]
    row = col
    print(row , new_grid)
    for i in range(row + 1, n - row - 2, -1):
        new_grid[i][row-2] = grid[i-1][row-2]
    print(row , col , new_grid)
    row , col = now + 1 , now + 1
    now += 1
    print(row , col)
print(new_grid)