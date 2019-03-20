class Solution:
    def isValidSudoku(self, board):
        return self.iscolvalid(board) and self.isrowvalid(board) and self.issquarevalid(board)

    def iscolvalid(self,board):
        for i in range(9):
            line=[]
            for j in range(9):
                line.append(board[j][i])
            if not self.isvalid(line):
                return False
        return True

    def isrowvalid(self,board):
        for line in board:
            if not self.isvalid(line):
                return False
        return True

    def issquarevalid(self,board):
        for i in range(0,9,3):
            for j in range(0,9,3):
                line=[]
                line+=board[i][j:j+3]
                line += board[i+1][j:j + 3]
                line += board[i+2][j:j + 3]
                if not self.isvalid(line):
                    return False
        return True

    def isvalid(self,line):
        seen=set()
        for item in line:
            if item != ".":
                if item in seen:
                    return False
                else:
                    seen.add(item)
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
print(s1.isValidSudoku(matrix))