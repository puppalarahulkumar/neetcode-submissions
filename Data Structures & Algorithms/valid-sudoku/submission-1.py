class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set=set()
            for j in range(9):
                item=board[i][j]
                if item in row_set:
                    return False
                elif item != ".":
                    row_set.add(item)
        #for column
        for i in range(9):
            column_set=set()
            for j in range(9):
                item=board[j][i]
                if item in column_set:
                    return False
                elif item != ".":
                    column_set.add(item)

        #for boxes
        variable = [(0,0),(0,3),(0,6),
                    (3,0),(3,3),(3,6),
                    (6,0),(6,3),(6,6)]

        for i,j in variable:
            s=set()
            for row in range(i,i+3):
                for column in range(j,j+3):
                    item=board[row][column]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
                    
        return True