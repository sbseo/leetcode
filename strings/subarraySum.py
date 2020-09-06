from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.dic = defaultdict(bool)
    
    def subarraySum(self, nums, k):
        self.dfs(nums, k, 0, len(nums)-1, sum(nums))
        return self.dic.values().count(True)

        
    def dfs(self, nums, k, idx1, idx2, curr_sum):
        #base
        if idx1>idx2 or self.dic[(idx1,idx2)]:
            return 

        if curr_sum == k:
            self.dic[(idx1,idx2)] = True
        else:
            self.dic[(idx1,idx2)] = False
        
        #recursion
        if idx1+1 < len(nums): 
            self.dfs(nums, k, idx1+1, idx2, curr_sum-nums[idx1])
        if idx2-1 >= 0:
            self.dfs(nums, k, idx1, idx2-1, curr_sum-nums[idx2])
        
        return 
        
                
