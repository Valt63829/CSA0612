# Question 4: Sorting Sensor Alerts by Severity
# Compare Plain Bubble Sort and Optimized Bubble Sort

def plain_bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    passes = 0
    comparisons = 0

    for i in range(n - 1):
        passes += 1
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a, passes, comparisons


def optimized_bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    passes = 0
    comparisons = 0

    for i in range(n - 1):
        swapped = False
        passes += 1

        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a, passes, comparisons


# -------------------------
# Example
# Severity: 1 = Critical, 5 = Low
# -------------------------
alerts = [1, 2, 3, 2, 4, 5, 3, 4, 5, 5, 4, 3, 2, 1, 2]

print("Original Alerts:", alerts)

plain_sorted, plain_passes, plain_comp = plain_bubble_sort(alerts)
opt_sorted, opt_passes, opt_comp = optimized_bubble_sort(alerts)

print("\nPlain Bubble Sort")
print("Sorted Alerts :", plain_sorted)
print("Passes        :", plain_passes)
print("Comparisons   :", plain_comp)

print("\nOptimized Bubble Sort")
print("Sorted Alerts :", opt_sorted)
print("Passes        :", opt_passes)
print("Comparisons   :", opt_comp)


# -------------------------
# Test Cases
# -------------------------
assert plain_bubble_sort([3, 2, 1])[0] == [1, 2, 3]
assert optimized_bubble_sort([3, 2, 1])[0] == [1, 2, 3]
assert optimized_bubble_sort([1, 2, 3])[1] == 1      # Early exit
assert optimized_bubble_sort([]) == ([], 0, 0)

print("\nAll test cases passed!")