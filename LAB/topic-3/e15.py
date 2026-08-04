text = "AAAAAAAAAB"
pattern = "AAAAB"

count = 0
found = False

for i in range(len(text) - len(pattern) + 1):
    j = 0
    while j < len(pattern):
        count += 1
        if text[i + j] != pattern[j]:
            break
        j += 1
    if j == len(pattern):
        found = True
        break

print("Comparisons =", count)

if count == len(pattern):
    print("Best Case")
elif found:
    print("Average Case")
else:
    print("Worst Case")