def search_tree(array: list, target: int, left, right) -> bool:
    if(left > right):
        return False
    
    mid = left + (right - left) // 2
    if(array[mid] == target):
        return True
    if(array[mid] > target):
        return search_tree(array, target, left, mid - 1)
    if(array[mid] < target):
        return search_tree(array, target, mid + 1, right)
    
    return False

target = 11
array = [1,3,5,6,7,10]
result = search_tree(array, target, 0, len(array) - 1)
print(result)