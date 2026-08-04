text = "AABAACAADAABAABA"
pattern = "AABA"

count = 0
for i in range(len(text) - len(pattern) + 1):
    j = 0
    while j < len(pattern):
        count += 1
        if text[i + j] != pattern[j]:
            break
        j += 1
    if j == len(pattern):
        print("Pattern found at position", i)

print("Total comparisons =", count)