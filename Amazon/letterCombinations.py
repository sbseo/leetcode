from itertools import product
import string

class Solution:
    def letterCombinations(self, digits: str):
        
        if not digits:
            return []
        
        letters = list()
        for digit in digits:
            digit = int(digit)
            if digit == 7: 
                letters.append(string.ascii_lowercase[(digit-2)*3:(digit-2)*3+4])
            elif digit == 8: 
                letters.append(string.ascii_lowercase[(digit-2)*3+1:(digit-2)*3+1+3])
            elif digit == 9: 
                letters.append(string.ascii_lowercase[(digit-2)*3+1:(digit-2)*3+4+1])
            else:
                letters.append(string.ascii_lowercase[(digit-2)*3:(digit-2)*3+3])
        
        letters = map(list, letters)
        ans = list(product(*letters))
    
        return list(map(''.join, ans))
            

print(Solution().letterCombinations("23")) #["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
