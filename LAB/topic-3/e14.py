text = "ABABABABAB"
pattern = "ABAB"

comp = match = mismatch = 0

for i in range(len(text) - len(pattern) + 1):
    for j in range(len(pattern)):
        comp += 1
        if text[i + j] == pattern[j]:
            match += 1
        else:
            mismatch += 1
            break

print("Comparisons =", comp)
print("Matches =", match)
print("Mismatches =", mismatch)