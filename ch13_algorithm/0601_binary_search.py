def search_binary(search_space, value):
    low = 0
    high = len(search_space) - 1
    while low <= high:
        middle = (low + high) // 2
        if search_space[middle] > value:
            high = middle - 1
        elif search_space[middle] < value:
            low = middle + 1
        else:
            return middle
    return -1


myList = [2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
print("인덱스=", search_binary(myList, 34))
