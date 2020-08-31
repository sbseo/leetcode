from itertools import groupby

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        S = self.groupify(S)
        answer = 0
        for word in words:
            query = self.groupify(word)
            if len(query) != len(S):    
                continue
            
            for j, q in enumerate(query):
                if S[j][0] != q[0] or S[j][1] < q[1]:
                    break
                if S[j][1] >= 3:
                    continue
                if S[j][1] < 3 and S[j][1] != q[1]:
                    break
            else:
                answer += 1
                            
        return answer
    
    def groupify(self, sen):
        return [(k, len(list(v))) for k, v in groupby(sen)]
            
        
        
        
        