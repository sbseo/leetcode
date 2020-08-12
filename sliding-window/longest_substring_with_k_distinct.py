from collections import Counter

def longest_substring_with_k_distinct(str, k):

    # create set for validation
    curr_counter = Counter()
    
    # create sliding window O(N)
    l, r = 0, 0
    length = 0
    
    while r < len(str)-1:
        # expand when less than k or equal to k, save answer
        if len(curr_counter.keys()) <= k:
            length = max(length, r-l+1)
            r += 1
            if r < len(str): curr_counter[str[r]] += 1
    
        # shrink when greater than K
        else:
            if curr_counter[str[l]] == 1: 
                curr_counter.pop(str[l])  
            else: 
                if curr_counter[str[l]]: curr_counter[str[l]] -= 1
            l += 1
    return length

print(longest_substring_with_k_distinct("araaci", 2)) # 4
print(longest_substring_with_k_distinct("araaci", 1)) # 2
print(longest_substring_with_k_distinct("cbbebi", 3)) # 5