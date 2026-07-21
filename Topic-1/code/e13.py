# Experiment 13: Maximum Subarray Sum
# Compare Kadane's Algorithm and Divide & Conquer

# -------------------------------
# Kadane's Algorithm - O(n)
# -------------------------------
def kadane(arr):
    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global


# -------------------------------
# Divide & Conquer - O(n log n)
# -------------------------------
def max_crossing_sum(arr, left, mid, right):
    # Maximum sum on left side
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    # Maximum sum on right side
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def divide_and_conquer(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = divide_and_conquer(arr, left, mid)
    right_max = divide_and_conquer(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


# -------------------------------
# Main Program
# -------------------------------
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

print("Array:", arr)
print("Kadane's Algorithm Maximum Sum:", kadane(arr))
print("Divide & Conquer Maximum Sum:", divide_and_conquer(arr, 0, len(arr) - 1))