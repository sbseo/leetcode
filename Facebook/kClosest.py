import math
import heapq

class MyNode:
    def __init__(self, idx, distance):
        self.distance = distance
        self.idx = idx
        
    def __lt__(self, other):
        return self.distance < other.distance
    
    def __repr__(self):
        return str(self.idx)
        
class Solution(object):
    def kClosest(self, points, K):
        min_heap = list()
        # distance List
        for i, point in enumerate(points):
            node = MyNode(i, math.sqrt(point[0]**2 + point[1]**2))
            heapq.heappush(min_heap, node)
        
        # get K points
        idxs = heapq.nsmallest(K, min_heap)
        return [points[int(str(idx))] for idx in idxs] 
    
print(Solution().kClosest([[1,3],[-2,2]], 1)) # [[-2,2]]