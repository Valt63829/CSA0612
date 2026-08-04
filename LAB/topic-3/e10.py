arr = [45, 23, 67, 12, 89, 34, 56, 78, 90, 11, 29, 73, 18, 64, 37]
keys = [73, 18, 100]

for key in keys:
    print("\nSearching for", key)
    count = 0
    found = False

    for x in arr:
        count += 1
        print("Compare with", x)
        if x == key:
            found = True
            break

    if found:
        print("Found")
    else:
        print("Not Found")

    print("Comparisons =", count)

print("\nComplexities")
print("Best Case : O(1)")
print("Average Case : O(n)")
print("Worst Case : O(n)")
print("Space Complexity : O(1)")