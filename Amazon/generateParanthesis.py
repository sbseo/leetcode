class Solution:
    def generateParenthesis(self, n: int):
        
        ans = list()
        self.dfs(n, 0, 0, ans, "")
        
        return ans
    
    def dfs(self, n, l, r, ans, curr):
        
        if r > l: return
        if r == n and l == n:
            ans.append(curr)
            return
        if l < n: 
            self.dfs(n, l+1,r, ans, curr + '(')
        if r < n : 
            self.dfs(n, l, r+1, ans, curr + ')')
        
print(Solution().generateParenthesis(3))