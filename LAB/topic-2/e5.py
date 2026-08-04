# Question 1: Exam Result Slip Correction
# Optimized Bubble Sort with Early Exit

def bubble_sort(arr):
    a = arr.copy()      # Keep original list unchanged
    n = len(a)
    passes = 0

    for i in range(n - 1):
        swapped = False
        passes += 1

        # Bubble the largest element to the end
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        # Stop if no swaps occurred
        if not swapped:
            break

    return a, passes


# -------------------------
# Example
# -------------------------
roll_numbers = [101, 102, 104, 103, 105, 106, 108, 107]

sorted_rolls, total_passes = bubble_sort(roll_numbers)

print("Original Roll Numbers:", roll_numbers)
print("Sorted Roll Numbers  :", sorted_rolls)
print("Passes Required      :", total_passes)


# -------------------------
# Test Cases
# -------------------------
assert bubble_sort([101,102,104,103,105])[0] == [101,102,103,104,105]
assert bubble_sort([1,2,3,4])[1] == 1          # Already sorted
assert bubble_sort([]) == ([], 0)              # Empty list
assert bubble_sort([5])[1] == 0                # Single element

print("All test cases passed!")