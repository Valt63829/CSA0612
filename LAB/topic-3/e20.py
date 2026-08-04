text = "TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
pattern = "TATCTT"

count = 0

for i in range(len(text) - len(pattern) + 1):
    print("Shift", i)
    j = 0
    while j < len(pattern):
        count += 1
        if text[i+j] != pattern[j]:
            break
        j += 1
    if j == len(pattern):
        print("Pattern found at position", i)

print("Total comparisons =", count)

print("\nComplexity")
print("Best Case : O(n)")
print("Worst Case : O(n*m)")
print("Space Complexity : O(1)")