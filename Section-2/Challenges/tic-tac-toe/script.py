
from pwn import *

io = process("./ttt")
counter = 0

def flatten(xss):
    return [x for xs in xss for x in xs]

def checkWin(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            return 1
        if grid[0][i] == grid[1][i] == grid[2][i]:
            return 1
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return 1
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return 1

def AmIWinningIn1Move(grid):
    for i in range(3):
        for j in range(3):
            if(grid[i][j]==0):
                grid[i][j] = 2
                if(checkWin(grid)):
                    return i,j
                else:
                    grid[i][j] = 0
    return -1,-1

def AmILosingIn1Move(grid):
    for i in range(3):
        for j in range(3):
            if(grid[i][j]==0):
                grid[i][j] = 1
                if(checkWin(grid)):
                    return i,j
                else:
                    grid[i][j] = 0
    return -1,-1

def moveNumber2(grid):
    if grid[0][0] == 1:
        return 2,2
    if grid[1][0] == 1:
        return 0,1
    if grid[0][1] == 1:
        return 1,0
    if grid[2][1] == 1:
        return 1,2
    if grid[1][2] == 1:
        return 2,1
    if grid[2][0] == 1:
        return 0,2
    if grid[0][2] == 1:
        return 2,0
    if grid[2][2] == 1:
        return 0,0
    
def moveNumber3(grid):
    if grid[0][1] == 2:
        return 0,0
    if grid[1][0] == 2:
        return 2,0
    if grid[2][1] == 2:
        return 2,2
    if grid[1][2] == 2:
        return 0,2
    if grid[1][2] == 1:
        return 2,1
    if grid[2][0] == 1:
        return 0,2
    if grid[0][2] == 1:
        return 2,0
    if grid[2][2] == 1:
        return 0,0

def solve(grid):
    x,y = AmIWinningIn1Move(grid)
    if(x!=-1):
        return x,y
    x,y = AmILosingIn1Move(grid)
    if x!=-1:
        return x,y
    #time for the STRATEGY lol
    n2s = 0
    for row in grid:
        for cell in row:
            if cell == 2:
                n2s +=1
    if n2s == 2:
        x,y = moveNumber2(grid)
        return x,y
    if n2s == 3:
        x,y = moveNumber3(grid)
    
    

