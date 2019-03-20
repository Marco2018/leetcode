class Solution:
    def isvalid(self,board,row,col,c):
        for i in range(9):
            if board[i][col]==c: return False
            if board[row][i]==c: return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:return False
        return True

    def solveSudoku(self, board):
        self.solve(board)
        return

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    for item in range(9):
                        c=chr(ord("1")+item)
                        if self.isvalid(board,i,j,c):
                            board[i][j]=c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True

s1=Solution()
matrix=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s1.solveSudoku(matrix))
print(matrix)