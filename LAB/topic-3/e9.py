matrix = [
    [12, 8, 15],
    [5, 18, 27],
    [9, 11, 24]
]

key = 24

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == key:
            print("Element found at Row", i + 1, "Column", j + 1)