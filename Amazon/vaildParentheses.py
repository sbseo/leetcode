class Solution:
    def isValid(self, s):
        
        if not s: return True
        stack = list()
        openings = ['[','(','{']
        closings = [']',')','}']
        for c in s:
            if c in openings:
                stack.append(c)
            elif not len(stack):
                return False
            elif c in closings and c == closings[openings.index(stack[-1])]:
                stack.pop()
            elif c in closings and c != closings[openings.index(stack[-1])]:
                return False
        return True if not stack else False
    
print(Solution().isValid("()"))
print(Solution().isValid("["))
print(Solution().isValid("]"))