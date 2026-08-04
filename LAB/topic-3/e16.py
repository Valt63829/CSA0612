text = "COMPUTERSCIENCE"
pattern = "SCI"

count = 0

for i in range(len(text) - len(pattern) + 1):
    j = 0
    while j < len(pattern):
        count += 1
        if text[i + j] != pattern[j]:
            break
        j += 1
    if j == len(pattern):
        print("First occurrence at position", i)
        print("Comparisons =", count)
        break