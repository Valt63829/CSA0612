# Question 2: Memory-Constrained Embedded Device
# Selection Sort with Swap Counter

def selection_sort(arr):
    a = arr.copy()       # Keep original array unchanged
    n = len(a)
    swap_count = 0

    for i in range(n - 1):
        min_index = i

        # Find the minimum element
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swap_count += 1

    return a, swap_count


# -------------------------
# Example
# -------------------------
readings = [30, 25, 40, 20, 35]

sorted_readings, swaps = selection_sort(readings)

print("Original Readings:", readings)
print("Sorted Readings :", sorted_readings)
print("Number of Swaps :", swaps)
print("Maximum Possible Swaps (n-1):", len(readings) - 1)

# -------------------------
# Test Cases
# -------------------------
assert selection_sort([30,25,40,20,35])[0] == [20,25,30,35,40]
assert selection_sort([1,2,3])[1] == 0          # Already sorted
assert selection_sort([]) == ([], 0)            # Empty array
assert selection_sort([5])[1] == 0              # Single element

print("All test cases passed!")