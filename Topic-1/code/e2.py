def binary_search(arr, key, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, left, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, right)

# Test
arr = [5, 10, 15, 20, 25]
key = 20
result = binary_search(arr, key)
print(f"Key found at index {result}" if result != -1 else "Key not found")