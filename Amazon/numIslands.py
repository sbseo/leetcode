class Solution:
    def __init__(self):
        self.V, self.NV = "0", "1"
    
    def numIslands(self, grid) -> int:
        
        count = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == self.NV: 
                    count += self.dfs((i,j), grid)
        return count
        
    def dfs(self, curr, matrix):
        dirs = [(1,0), (0, 1), (-1,0), (0,-1)]    
        for v, h in dirs:
            next_row, next_col = curr[0] + v, curr[1] + h
            if self.isConnected((next_row, next_col), matrix) and matrix[next_row][next_col] == self.NV:
                matrix[next_row][next_col] = self.V
                self.dfs((next_row, next_col), matrix)
        return 1
            
    def isConnected(self, next_pos, matrix):
        row_len, col_len = len(matrix), len(matrix[0])
        if 0 <= next_pos[0] < row_len and 0 <= next_pos[1] < col_len:
            return True
        return False
    
print(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
