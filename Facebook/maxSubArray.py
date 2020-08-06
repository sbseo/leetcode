class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        
        cached = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums, 1):
            max_num = max(cached[i-1]+num, num)
            if i < len(nums): cached[i] = max_num
            
        return max(max(cached[1:]), max_num)
