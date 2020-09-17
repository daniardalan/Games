
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def get_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i,j

    return None 

def display_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 or i == 0:
            print(" ------------------------- ")

        for j in range(len(grid[0])):
            if j == 0:
                print(" | ", end="")
            elif j % 3 == 0:
                print("| ", end="") 
            if j == 8:
                print(str(grid[i][j]) + " | ")
            else:
                print(str(grid[i][j]) + " ", end="")
    print(" ------------------------- ")

def is_valid(grid, num, cell):
    row, col = cell
    for i in range(len(grid)):
        if grid[row][i] == num and col != i:
            return False
      
    for i in range(len(grid)):
        if grid[i][col] == num and row != i:
            return False
    
    x_box = col // 3
    y_box = row // 3

    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if grid[i][j] == num and (i,j) != cell:
                return False

    return True 

def solve(grid):
    empty = get_empty(grid)
    if not empty: 
        return True
    else: 
        row, col = empty
    
    for i in range(1,10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False 

display_grid(grid)
solve(grid)
display_grid(grid)