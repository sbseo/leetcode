def search_next_letter(letters, key):
    # TODO: Write your code here
    
    # 1. initialization
    l, r = 0, len(letters)-1
    if key > letters[-1]: return letters[0]
    
    # 2. binary search | O(log n)
    while l <= r:
        m = (l+r) // 2
        if letters[m] == key: 
            return letters[m+1]
        elif key > letters[m]:
            l = m+1
        elif key < letters[m]:
            r = m-1
    return letters[l % len(letters)]

def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f')) # h
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b')) # c
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm')) # a
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm')) # a


main()