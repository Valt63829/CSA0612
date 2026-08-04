# Question 3: Library Book Reordering
# Selection Sort with Physical Move Counter

def selection_sort_books(book_ids):
    books = book_ids.copy()      # Keep original list unchanged
    n = len(books)

    comparisons = 0
    physical_moves = 0

    for i in range(n - 1):
        min_index = i

        # Find the smallest book ID
        for j in range(i + 1, n):
            comparisons += 1
            if books[j] < books[min_index]:
                min_index = j

        # Physical move (swap) only if needed
        if min_index != i:
            books[i], books[min_index] = books[min_index], books[i]
            physical_moves += 1

    return books, comparisons, physical_moves


# -------------------------
# Example
# -------------------------
book_ids = [105, 101, 109, 103, 102, 108, 104, 106, 107]

sorted_books, comparisons, moves = selection_sort_books(book_ids)

print("Original Book IDs :", book_ids)
print("Sorted Book IDs   :", sorted_books)
print("Comparisons       :", comparisons)
print("Physical Moves    :", moves)
print("Maximum Moves (n-1):", len(book_ids) - 1)

# -------------------------
# Test Cases
# -------------------------
assert selection_sort_books([3, 1, 2])[0] == [1, 2, 3]
assert selection_sort_books([1, 2, 3])[2] == 0      # Already sorted
assert selection_sort_books([]) == ([], 0, 0)       # Empty list
assert selection_sort_books([5])[2] == 0            # Single book

print("All test cases passed!")