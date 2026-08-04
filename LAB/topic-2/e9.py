# Question 5: Card Game Hand Sorting
# Compare Bubble Sort on a Nearly Sorted Hand vs a Fully Shuffled Hand

def bubble_sort(arr):
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

        # Stop early if already sorted
        if not swapped:
            break

    return a, passes, comparisons


# -------------------------
# Nearly Sorted Hand
# -------------------------
hand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_card = 1

hand.append(new_card)

print("Nearly Sorted Hand:")
print("Before Sorting:", hand)

sorted_hand, passes1, comp1 = bubble_sort(hand)

print("After Sorting :", sorted_hand)
print("Passes        :", passes1)
print("Comparisons   :", comp1)


# -------------------------
# Fully Shuffled Hand
# -------------------------
shuffled_hand = [7, 2, 12, 4, 10, 1, 9, 13, 6, 3, 11, 5, 8]

print("\nFully Shuffled Hand:")
print("Before Sorting:", shuffled_hand)

sorted_shuffle, passes2, comp2 = bubble_sort(shuffled_hand)

print("After Sorting :", sorted_shuffle)
print("Passes        :", passes2)
print("Comparisons   :", comp2)


# -------------------------
# Test Case
# -------------------------
assert bubble_sort([2, 3, 4, 1])[0] == [1, 2, 3, 4]
assert bubble_sort([4, 3, 2, 1])[0] == [1, 2, 3, 4]
assert bubble_sort([]) == ([], 0, 0)

print("\nAll test cases passed!")