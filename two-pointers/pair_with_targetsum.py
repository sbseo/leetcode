def pair_with_targetsum(arr, target_sum):
    
    # method 1) use cominations O(n!)
    # method 2) two pointers O(N)
    
    # initialize pointers
    l, r  = 0, len(arr)-1
    
    while l < r < len(arr): 
        curr_sum = arr[l] + arr[r]
        if curr_sum == target_sum:
            return [l, r]
        # shrink
        elif curr_sum > target_sum:
            r -= 1
        # expand
        elif curr_sum < target_sum:
            l += 1
    return [-1]

print(pair_with_targetsum([1,2,3,4,6], 6)) # [1,3]
print(pair_with_targetsum([2,5,9,11], 11)) # [0,2]