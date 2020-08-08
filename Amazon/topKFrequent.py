from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        counter = Counter(words)
        l = list()
        for word, count in counter.items():
            heapq.heappush(l, (word,-count))
        return list(map(lambda x: x[0],heapq.nsmallest(k, l, key=lambda x: (x[1],x[0]))))
    
print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2)) # ["i","love"]
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)) #["the", "is", "sunny", "day"]s
print(Solution().topKFrequent(["aaa",'aa','a'], 1)) #["a"]
print(Solution().topKFrequent(["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]
,1)) #["fvvdtpnzx"]