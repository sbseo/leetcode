import heapq

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        heapq.heapify(nums1)
        for v in nums2:
            heapq.heappush(nums1, v)
    
        l, r = 0, len(nums1)-1
        m = (l+r) / 2
        
        for _ in range(int(m)):
            heapq.heappop(nums1)
    
        if m == int(m):
            return float(heapq.heappop(nums1))
        return float((heapq.heappop(nums1) + heapq.heappop(nums1)) / 2)
    
print(Solution().findMedianSortedArrays([1,2], [3,4])) # 2.5
print(Solution().findMedianSortedArrays([3], [-2,-1])) # -1
print(Solution().findMedianSortedArrays([], [-1])) # -1
print(Solution().findMedianSortedArrays([], [2,3])) # 2.5
