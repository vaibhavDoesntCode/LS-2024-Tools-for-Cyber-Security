#flag{4r3_y0u_r3411y_hum4n??}

from pwn import *

def checkWin(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != 0:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != 0:
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != 0:
        return grid[0][2]
    empty = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                empty += 1
    if empty == 0:
        return 0          
    
    return -2

def minimax(grid, depth, is_maximizing):
    result = checkWin(grid)
    if result != -2:
        return result
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    score = minimax(grid, depth + 1, False)
                    grid[i][j] = 0
                    best_score = max(best_score, score)
        return best_score
        
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                    score = minimax(grid, depth + 1, True)
                    grid[i][j] = 0
                    best_score = min(best_score, score)
        return best_score

def bestMove(grid):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    
    best_score = -float('inf')
    best_move = (-1, -1)
    for cell in empty_cells:
        grid[cell[0]][cell[1]] = 1
        score = minimax(grid, 0, False)
        grid[cell[0]][cell[1]] = 0
        if score > best_score:
            best_score = score
            best_move = cell

    return best_move

def featureChangingLol(x):
    return {'x': -1, 'o': 1}.get(x, 0)

if __name__ == '__main__':
    io = process("./ttt")

    io.recvuntil('Enter the block')
    io.recvline()
    io.send(b'1,1\n')
    while True:
        grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        while( checkWin(grid)==-2):
            line1 = (io.recvline()).decode().split()
            if(line1[0]=='Game'):
                continue
            line2 = (io.recvline()).decode().split()
            line3 = (io.recvline()).decode().split()
            for i in range(3):
                grid[0][i] = featureChangingLol(line1[i])
                grid[1][i] = featureChangingLol(line2[i])
                grid[2][i] = featureChangingLol(line3[i])

            (x,y) = bestMove(grid)
            grid[x][y] = 1
            io.recvline()
            io.send(f"{x},{y}\n".encode())
        
        x = (io.recvline()).decode()
        print(x)
        if(x.split()[0]=="You"):
            y = (io.recvline()).decode()
            print(y)




    io.interactive()