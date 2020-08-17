def remove_duplicates(arr):
    
    return sorted(list(set(arr)))

print(remove_duplicates([2,3,3,3,6,9,9])) #4
print(remove_duplicates([2,2,2,11])) #2