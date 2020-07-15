from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        answer = list()
        answer_exists = False
        while l <= r <= len(s):
            window = Counter(s[l:r])
            if not len(Counter(t) - window):
                answer_exists = True
                answer.append(s[l:r])
                l += 1
            else:
                r +=1
        return answer if answer_exists else ""

print(Solution().minWindow("ADOBECODEBANC", "ABC")) #BANC
print(Solution().minWindow("ab", "a")) #a
print(Solution().minWindow("bbaa", "aba")) #baa
print(Solution().minWindow("ab", "a")) #a
print(Solution().minWindow("a", "a")) #a
print(Solution().minWindow("a", "aa")) # ""
print(Solution().minWindow("coobdafceeaxab", "abc")) # bdafc
print(Solution().minWindow("ADOBECODEBANC", "ABC")) # BANC