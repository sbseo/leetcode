from collections import defaultdict

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        dic = defaultdict(int)
        for v1, v2 in similarPairs:
            dic[(v1,v2)] += 1
        
        # 1. Length of the sentence should be the same
        if len(sentence1) != len(sentence2):
            return False
        
        # 2. Compare each similar pairs
        print(dic)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and (not dic[(w1,w2)] and not dic[(w2,w1)]):
                return False
        
        return True
