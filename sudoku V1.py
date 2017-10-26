# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:33:39 2017

@author: santh
"""

#sudoku=[6,0,0,8,0,5,1,0,0,0,0,1,0,0,0,0,3,0,5,0,0,7,0,0,0,6,9,0,0,2,0,0,9,0,4,6,1,0,4,0,0,0,7,0,5,9,7,0,6,0,0,2,0,0,2,1,0,0,0,3,0,0,7,0,3,0,0,0,0,6,0,0,0,0,6,5,0,7,0,0,4]
sudoku=[5,7,0,0,0,6,0,0,3,2,3,0,7,9,0,0,4,8,0,0,6,8,3,0,0,0,0,6,0,0,0,2,0,0,5,0,0,2,3,0,0,0,7,6,0,0,9,0,0,6,0,0,0,4,0,0,0,0,1,2,5,0,0,1,6,0,0,7,3,0,8,2,3,0,0,6,0,0,0,9,7]
#sudoku=[9,0,0,7,3,8,4,0,0,8,7,0,0,0,0,1,9,3,3,2,0,9,0,5,0,0,0,5,0,7,0,0,0,0,0,0,0,3,0,5,0,6,0,8,0,0,0,0,0,0,0,3,0,2,0,0,0,2,0,1,0,6,9,2,1,8,0,0,0,0,3,4,0,0,9,3,7,4,0,0,8]
#sudoku=[4,0,0,0,0,6,0,0,0,6,3,2,0,5,0,0,0,8,0,0,0,0,0,7,9,6,0,0,0,0,0,0,0,8,0,6,0,0,5,0,3,0,4,0,0,9,0,1,0,0,0,0,0,0,0,5,7,9,0,0,0,0,0,8,0,0,0,7,0,1,5,3,0,0,0,5,0,0,0,0,9]
row_indices=[[0,1,2,3,4,5,6,7,8],
             [9,10,11,12,13,14,15,16,17],
             [18,19,20,21,22,23,24,25,26],
             [27,28,29,30,31,32,33,34,35],
             [36,37,38,39,40,41,42,43,44],
             [45,46,47,48,49,50,51,52,53],
             [54,55,56,57,58,59,60,61,62],
             [63,64,65,66,67,68,69,70,71],
             [72,73,74,75,76,77,78,79,80]]
col_indices=[[0,9,18,27,36,45,54,63,72],
             [1,10,19,28,37,46,55,64,73],
             [2,11,20,29,38,47,56,65,74],
             [3,12,21,30,39,48,57,66,75],
             [4,13,22,31,40,49,58,67,76],
             [5,14,23,32,41,50,59,68,77],
             [6,15,24,33,42,51,60,69,78],
             [7,16,25,34,43,52,61,70,79],
             [8,17,26,35,44,53,62,71,80]]
box_indices=[[0,1,2,9,10,11,18,19,20],
             [27,28,29,36,37,38,45,46,47],
             [54,55,56,63,64,65,72,73,74],
             [3,4,5,12,13,14,21,22,23],
             [30,31,32,39,40,41,48,49,50],
             [57,58,59,66,67,68,75,76,77],
             [6,7,8,15,16,17,24,25,26],
             [33,34,35,42,43,44,51,52,53],
             [60,61,62,69,70,71,78,79,80]]
def constraintLogic(rows,cols,boxes,s):
    for i in range(1,10):
        position=[]
        for j in range(0,9):
            position=[]
            for k in range(0,9):
                if i in rows[j][k]:
                    position.append(j)
                    position.append(k)
            if len(position)==2:
                s[row_indices[position[0]][position[1]]]=i
    for i in range(1,10):
        position=[]
        for j in range(0,9):
            position=[]
            for k in range(0,9):
                if i in cols[j][k]:
                    position.append(j)
                    position.append(k)
            if len(position)==2:
                s[col_indices[position[0]][position[1]]]=i
    for i in range(1,10):
        position=[]
        for j in range(0,9):
            position=[]
            for k in range(0,9):
                if i in boxes[j][k]:
                    position.append(j)
                    position.append(k)
            if len(position)==2:
                s[box_indices[position[0]][position[1]]]=i
    return s                    
def notsolved(var):
    for i in var:
        if i==0:
            return True
    return False
def update_Matrices(var):
    rows=[]
    cols=[]
    boxes=[]
    sub_list=[]
    for i in row_indices:
        for j in i:
            sub_list.append(var[j])
        rows.append(sub_list)
        sub_list=[]
    for i in col_indices:
        for j in i:
            sub_list.append(var[j])
        cols.append(sub_list)
        sub_list=[]
    for i in box_indices:
        for j in i:
            sub_list.append(var[j])
        boxes.append(sub_list)
        sub_list=[]
    return rows,cols,boxes
def find(var,what):
    Number=[]
    Position=[]
    for  i in range(1,10):
        count=0
        for j in var:
            for k in j:
                if i in k:
                    count+=1
                    if what=="row":
                        position=row_indices[j][k]
                    elif what=="col":
                        position=col_indices[j][k]
                    else:
                        position=box_indices[j][k]
        if count==1:
            Number.append(i)
            Position.append(position)
    return Number,Position
def satisfies(i,j,rows,cols,boxes):
    ROW=0
    COL=0
    BOX=0
    for x in range(0,9):
            if i in row_indices[x]:
                ROW=x
    for x in range(0,9):
            if i in col_indices[x]:
                COL=x
    for x in range(0,9):
            if i in box_indices[x]:
                BOX=x
    if j not in rows[ROW] and j not in cols[COL] and j not in boxes[BOX]:
        return True
    else:
        return False
def IterationsList(s):
    rows,cols,boxes=update_Matrices(s)
    Possibilities=[]
    for i in range(0,81):
        sub_list=[]
        if s[i]==0:
            for j in range(1,10):
                if satisfies(i,j,rows,cols,boxes):
                    sub_list.append(j)
        else:
            sub_list.append(s[i])
        Possibilities.append(sub_list)
    for i in range(0,81):
            if len(Possibilities[i])==1:
                s[i]=Possibilities[i][0]
    global rP,cP,bP
    rP,cP,bP=update_Matrices(Possibilities)
    s=constraintLogic(rP,cP,bP,s)
    return s
def PrintSudoku(sudoku):
    i=0
    print "\n"
    while i<81:
            print sudoku[i],sudoku[i+1],sudoku[i+2],sudoku[i+3],sudoku[i+4],sudoku[i+5],sudoku[i+6],sudoku[i+7],sudoku[i+8]
            i+=9
    print "\n"
def MainFunc(s):
    totalIterations=0
    #print "\nthe entered sudoku is"
    #PrintSudoku(s)
    while notsolved(s) and totalIterations<100:
        totalIterations+=1
        s=IterationsList(s)
    print "\nthe sudoku after " + str(totalIterations)+" iterations with constraintLogic is: "
    PrintSudoku(s)
if __name__=='__main__':
    MainFunc(sudoku)    
