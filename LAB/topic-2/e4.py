# Question 4: Contest Prize Distribution
# Selection Sort (Descending Order)

def prize_distribution(participants):
    # Make a copy to keep original list unchanged
    arr = participants.copy()
    n = len(arr)

    print("Prize Distribution (Ranking):")

    # Selection Sort in Descending Order
    for i in range(n):
        max_index = i

        # Find participant with highest score
        for j in range(i + 1, n):
            if arr[j][1] > arr[max_index][1]:
                max_index = j

        # Swap into correct position
        arr[i], arr[max_index] = arr[max_index], arr[i]

        # Print current ranked participant
        print(f"Rank {i+1}: {arr[i][0]} (Score: {arr[i][1]})")

    return arr


# -------------------------
# Example
# -------------------------
participants = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
]

ranking = prize_distribution(participants)

print("\nFinal Ranking:")
print(ranking)


# -------------------------
# Test Cases
# -------------------------
assert prize_distribution([("A", 50), ("B", 80), ("C", 70)]) == [
    ("B", 80), ("C", 70), ("A", 50)
]

assert prize_distribution([]) == []

assert prize_distribution([("Only", 100)]) == [("Only", 100)]

print("\nAll test cases passed!")