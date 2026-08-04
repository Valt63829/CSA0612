# Selection Sort - Find Top K Scores (Maximum Repeatedly)

def top_k_scores(scores, k):
    arr = scores.copy()      # Keep original list unchanged
    n = len(arr)

    if n == 0:
        return []

    k = min(k, n)            # Handle case where k > number of scores

    # Find the maximum repeatedly
    for i in range(k):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap maximum element to the front
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr[:k]


# -------------------------
# Example
# -------------------------
scores = [72, 88, 65, 90, 77, 95, 60, 83, 91, 68]
print("Top 5 Scores:", top_k_scores(scores, 5))

# -------------------------
# Test Cases
# -------------------------
assert top_k_scores([72,88,65,90,77,95,60,83,91,68], 5) == [95,91,90,88,83]
assert top_k_scores([5,3,1], 5) == [5,3,1]      # fewer than k items
assert top_k_scores([], 3) == []                # empty input

print("All test cases passed!")