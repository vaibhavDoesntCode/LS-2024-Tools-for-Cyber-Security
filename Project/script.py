# flag is GJVWUSSL[[QOESXVZVULWY^WQL[W^XO

from pwn import *
import numpy as np

def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:                        
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3)
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        grid[i][j] = 0
        return False


io = process('./sudoku') 
io.recvline()
io.recvline()
io.recvline()



while True:
    output = io.recvuntil("E")
    matrix = np.zeros(shape=(9,9), dtype=int)
    row, col = 0, 0
    reached = False
    for indi in output:
        
    
        char = chr(indi)
        if '1' <= char <= '9':
            matrix[row][col] = int(char)
            col += 1
        elif char == '.':
            matrix[row][col] = 0
            col += 1
        
        if col >= 9:
            col = 0
            row += 1
    matrixInitial  = matrix.copy()
    solved = solveSudoku(matrix)

    io.recvuntil(":")
    for i in range(9):
        for j in range(9):
                if matrixInitial[i][j] == 0:
                        io.send(f"{i} {j} {matrix[i][j]}\n".encode())
                        print(line)
                        for k in range(14):
                                io.recvline()  
                                                    
                        io.recvuntil(":")



io.interactive()