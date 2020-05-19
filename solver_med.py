#
#   author:     Brice Gibson
#   Version:    V.01
#   Date:       05/15/2020
#   Comments:   solves easy sudoku using row, column and box match
#

import numpy as nmp

def make_box(grid):
    #arrange results in box format
    a = nmp.array(grid[0:3])
    top_box = nmp.array(
        [[a[..., 0], a[..., 1], a[..., 2]], [a[..., 3], a[..., 4], a[..., 5]], [a[..., 6], a[..., 7], a[..., 8]]])
    a = nmp.array(grid[3:6])
    middle_box = nmp.array(
        [[a[..., 0], a[..., 1], a[..., 2]], [a[..., 3], a[..., 4], a[..., 5]], [a[..., 6], a[..., 7], a[..., 8]]])
    box = nmp.array([top_box,middle_box])
    a = nmp.array(grid[6:9])
    bottom_box = nmp.array(
        [[a[..., 0], a[..., 1], a[..., 2]], [a[..., 3], a[..., 4], a[..., 5]], [a[..., 6], a[..., 7], a[..., 8]]])
    box = nmp.array([top_box,middle_box,bottom_box])
    return box



def solve():
    # simple row column match
    for n in sudoku_to_solve:
        vals = {1, 2, 3, 4, 5, 6, 7, 8, 9} # create a set

        # remove all values in the same row
        vals = set(vals) - set(sudoku_row[n[1]])

        # remove all values in the same column
        vals = set(vals) - set(sudoku_col[n[0]])

        # remove all values in same group (box)
        vals = set(vals) - set(sudoku_box[n[2][0]][n[2][1]][0]) - set(sudoku_box[n[2][0]][n[2][1]][1]) - set(
            sudoku_box[n[2][0]][n[2][1]][2])

        if len(vals) == 1:
            #print("Grid: " + str(n) + " Value: " + str(vals) + " Row: " + str(sudoku_row[n[1]]) + " Col: " + str(sudoku_col[n[0]]))

            sudoku_row[n[1]][n[0]] = list(vals)[0]      # update the sudoko row
            sudoku_to_solve.remove(n)                   # remove from the solver array


#######################################################################################################################

# Easy
# sudoku_row = nmp.array(([6, 3, 0, 2, 0, 8, 0, 1, 0],
#             [2, 0, 0, 0, 5, 0, 0, 8, 9],
#             [1, 0, 9, 0, 6, 0, 0, 3, 0],
#             [0, 0, 8, 0, 0, 6, 0, 5, 0],
#             [0, 0, 0, 1, 8, 7, 0, 0, 0],
#             [0, 6, 0, 5, 0, 0, 9, 0, 0],
#             [0, 9, 0, 0, 7, 0, 1, 0, 6],
#             [8, 1, 0, 0, 2, 0, 0, 0, 5],
#             [0, 2, 0, 4, 0, 3, 0, 9, 7]))

# sudoku_row = nmp.array((
#             [0, 0, 0, 1, 0, 0, 0, 4, 0],
#             [1, 9, 5, 0, 0, 8, 0, 0, 0],
#             [3, 4, 0, 0, 2, 0, 1, 0, 9],
#             [0, 0, 0, 9, 1, 0, 5, 0, 0],
#             [6, 0, 9, 8, 0, 2, 4, 0, 7],
#             [0, 0, 1, 0, 3, 4, 0, 0, 0],
#             [2, 0, 8, 0, 4, 0, 0, 7, 1],
#             [0, 0, 0, 7, 0, 0, 8, 3, 2],
#             [0, 1, 0, 0, 0, 9, 0, 0, 0]))

#Medium
sudoku_row = nmp.array((
            [1, 3, 0, 8, 0, 0, 6, 0, 0],
            [0, 0, 2, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 7, 9],
            [2, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 3, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 3],
            [5, 7, 0, 0, 8, 3, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 9, 0, 0],
            [0, 0, 9, 0, 0, 2, 0, 6, 7]))


# set all the sudoku data in rows, columns and boxes. We will solve the row
print(sudoku_row)
sudoku_col = sudoku_row.transpose()
sudoku_box = make_box(sudoku_row)

# these are the coordinates of any unsolved (0) cells in the sudoku
sudoku_to_solve = []
x = y = zb = za = 0
for r in sudoku_row:
    x = 0
    for rr in r:
        if rr == 0:
            if 0 <= x <= 2:
                zb = 0
            elif 3 <= x <= 5:
                zb = 1
            elif 6 <= x <= 8:
                zb = 2

            if 0 <= y <= 2:
                za = 0
            elif 3 <= y <= 5:
                za = 1
            elif 6 <= y <= 8:
                za = 2
            sudoku_to_solve.append([x, y, [za, zb]])
        x += 1
    y += 1

t = 0
while len(sudoku_to_solve) > 0:
    if t == len(sudoku_to_solve):
        break
    else:
        t = len(sudoku_to_solve)
        solve()
        sudoku_col = sudoku_row.transpose()
        sudoku_box = make_box(sudoku_row)
        #print(sudoku_row)
        # print(sudoku_col)
        # print(sudoku_box)

print(sudoku_row)
print(len(sudoku_to_solve))
