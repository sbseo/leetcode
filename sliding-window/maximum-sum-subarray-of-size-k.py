from collections import deque

def max_sub_array_of_size_k(k, arr):
    
    # create window
    window = deque(arr[:k])
    max_num = sum(window)
    
    # traverse with window: O(N)
    for element in arr[k:]:
        window.popleft()
        window.append(element)
        max_num = max(sum(window), max_num)
  
    return max_num

print(max_sub_array_of_size_k(3, [2,1,5,1,3,2])) # 9
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])) # 7