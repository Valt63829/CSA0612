arr = [3, 6, 9, 12, 15, 18, 21]
key = 15

comparisons = 0
matches = 0
mismatches = 0

for x in arr:
    comparisons += 1
    if x == key:
        matches += 1
    else:
        mismatches += 1

print("Total comparisons =", comparisons)
print("Total matches =", matches)
print("Total mismatches =", mismatches)