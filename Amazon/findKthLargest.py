import heapq

class Solution:
    def findKthLargest(self, nums, k):
        
        heapq.heapify(nums)
            
        return heapq.nlargest(k, nums)[k-1]
    
print(Solution().findKthLargest([3,2,1,5,6,4], 2)) # 5
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
