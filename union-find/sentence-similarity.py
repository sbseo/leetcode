from collections import defaultdict

# Union-Find (Transitive relation)
class MyClass:
    def __init__(self, numbers):
        self.dic = defaultdict(int)
        for v in numbers:
            self.dic[v] = v
            
    def find(self, a, b):
        return self.dic[a] == self.dic[b]
    
    def union(self, a, b):
        
        new_set = min(self.dic[a], self.dic[b])
        old_set = max(self.dic[b], self.dic[a])
        
        for k, v in self.dic.items():
            if v == old_set:
                self.dic[k] = new_set
        
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        
        # 0. Length of the sentence should be the same
        if len(words1) != len(words2):
            return False
        
        # 1. Initialize
        dic = defaultdict(set)
        all_numbers = set()
        for v1, v2 in pairs:
            all_numbers.add(v1)
            all_numbers.add(v2)
        for v1, v2 in zip(words1, words2):
            all_numbers.add(v1)
            all_numbers.add(v2)
        UF = MyClass(all_numbers)
                
        # 2. Compare each similar pairs
        for w1, w2 in pairs:
            if not UF.find(w1, w2):
                UF.union(w1, w2)
        
        for w1, w2 in zip(words1, words2):
            if not UF.find(w1, w2):
                return False
        return True
