class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
       
        num1, num2 = (map(int, v.split(".")) for v in (version1, version2))
        num1, num2 = list(num1), list(num2)
        d = len(num2) - len(num1)
        
        num1 += [0]*d 
        num2 += [0]*-d 
        
        if num1 > num2: return 1
        if num1 == num2: return 0
        if num1 < num2: return -1
            
print(Solution().compareVersion("0.1", "1.1")) # -1
print(Solution().compareVersion("1.0.1", "1")) # 1
print(Solution().compareVersion("7.5.2.4", "7.5.3")) # -1
print(Solution().compareVersion("1.0", "1.0.0")) # 0
print(Solution().compareVersion("01", "1")) # 0
print(Solution().compareVersion("1.2", "1.10")) # -1
