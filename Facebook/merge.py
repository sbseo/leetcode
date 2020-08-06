class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []
        
        # Sort intervals 
        intervals.sort(key=lambda x: x[0])
        
        # Convert to range of set
        sets = [set(range(l[0], l[1]+1)) for l in intervals]
        
        # Find intersection. If not append. 
        answer = list()
        curr = sets.pop(0)
        while sets:
            if curr - sets[0] != curr:
                curr |= sets.pop(0)
            else:
                answer.append(list(curr))
                curr = sets.pop(0)
        if curr: answer.append(list(curr))
        return [[min(ans), max(ans)] for ans in answer]
        
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]