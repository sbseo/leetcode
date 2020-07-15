class Solution:
    def missingNumber(self, nums):

        return (set(range(len(nums)+1)) - set(nums)).pop()

        
print(Solution().missingNumber([3,0,1])) # 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1])) # 8
print(Solution().missingNumber([0])) # 8
