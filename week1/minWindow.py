from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        target = Counter(t)
        answer, answer_exists = str(1) * (len(s)+1), False
        window = Counter(s[l:r+1])
        while r < len(s):
            if (target - window):
                r += 1
                if r < len(s): window[s[r]] += 1
            else:
                answer_exists = True
                if len(answer) > len(s[l:r+1]): answer = s[l:r+1]
                window[s[l]] -= 1
                l += 1
        return answer if answer_exists else ""

print(Solution().minWindow("ADOBECODEBANC", "ABC")) #BANC
print(Solution().minWindow("ab", "a")) #a
print(Solution().minWindow("bbaa", "aba")) #baa
print(Solution().minWindow("ab", "a")) #a
print(Solution().minWindow("a", "a")) #a
print(Solution().minWindow("a", "aa")) # ""
print(Solution().minWindow("coobdafceeaxab", "abc")) # bdafc
print(Solution().minWindow("ADOBECODEBANC", "ABC")) # BANC