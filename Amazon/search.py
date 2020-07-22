import numpy as np

class Solution:
    def search(self, nums, target) -> int:
        
        if len(set([target]) - set(nums)):
            return -1
        nums = np.array(nums)
        
        return np.where(target == nums)[0][0]

print(Solution().search([4,5,6,7,0,1,2], 0)) # 4
print(Solution().search([4,5,6,7,0,1,2], 3)) # 0