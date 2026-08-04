# Question 3: Bubble Sort Visualization Tool
# Prints the array after every pass

def bubble_sort_visualization(arr):
    a = arr.copy()      # Keep original array unchanged
    n = len(a)
    frames = []         # Store array after each pass

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        # Store current state after each pass
        frames.append(a.copy())
        print(f"Pass {i + 1}: {a}")

        # Stop early if already sorted
        if not swapped:
            break

    return frames


# -------------------------
# Example
# -------------------------
numbers = [5, 1, 4, 2, 8]

print("Original Array:", numbers)

frames = bubble_sort_visualization(numbers)

print("\nSorted Array:", frames[-1] if frames else numbers)


# -------------------------
# Test Cases
# -------------------------
assert bubble_sort_visualization([3, 2, 1])[-1] == [1, 2, 3]
assert bubble_sort_visualization([1, 2, 3])[0] == [1, 2, 3]
assert bubble_sort_visualization([]) == []

print("\nAll test cases passed!")