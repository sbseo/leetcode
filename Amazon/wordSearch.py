from collections import deque

class Solution:
    def exist(self, board, word):
        
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                q = deque(word)
                visited = [[False]*len(board[0]) for _ in board]
                visited[i][j] = True        
                curr = q.popleft()
                if curr == board[i][j] and self.dfs((i,j), board, visited, q):
                    return True
        return False
    
    def dfs(self, curr, board, visited, q):
        
        if not q:
            return True
        
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        for d in directions:
            next_row, next_col = curr[0] + d[0], curr[1] + d[1]
            if self.isConnected((next_row, next_col), board) and not visited[next_row][next_col] and q[0] == board[next_row][next_col]:
                visited[next_row][next_col] = True
                temp = q.popleft()
                if self.dfs((next_row, next_col), board, visited, q):
                    return True
                visited[next_row][next_col] = False
                q.insert(0, temp)
        return False

    def isConnected(self, next_pos, board):
        next_row, next_col = next_pos
        if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]): return True
        return False
        
        
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
, "ABCCED")) #True
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
, "SEE")) #True
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
, "ABCB")) #False
print(Solution().exist([["A"]]
, "A")) #True
print(Solution().exist([["A"]]
, "B")) #False
print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]]
, "AAB")) #True
