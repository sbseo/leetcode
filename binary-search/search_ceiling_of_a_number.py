def search_ceiling_of_a_number(arr, key):
    # TODO: Write your code here
    if key > arr[-1]: return -1
    
    l, r = 0, len(arr)-1
    while l < r:
        m = (l+r) // 2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            r = m-1
        elif arr[m] < key:
            l = m+1
    return l

def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()