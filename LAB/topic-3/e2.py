arr = [5, 10, 15, 20, 25, 30, 35]
key = 18

found = False
for i in range(len(arr)):
    if arr[i] == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
    print("Number of comparisons =", len(arr))