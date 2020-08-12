def smallest_subarray_with_given_sum(s, arr):
    
    # Two pointers O(N)    
    l, r = 0, 0
    _sum = arr[0]
    min_length = float('+inf')
    
    while r < len(arr):
        # expand when sum is smaller
        if _sum < s:   
            r += 1
            if r < len(arr): _sum += arr[r]
        
        # shrink when sum is greater or equal
        # save answer
        else:
            min_length = min(min_length, r-l+1)
            _sum -= arr[l]
            l += 1
    return min_length

print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2])) # 2
print(smallest_subarray_with_given_sum(7, [2,1,5,2,8])) # 1
print(smallest_subarray_with_given_sum(8, [3,4,1,1,6])) # 3