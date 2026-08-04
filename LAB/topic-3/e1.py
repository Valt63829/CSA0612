arr = [12, 25, 8, 45, 32, 19, 50]
key = 32

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        print("Number of comparisons =", i + 1)
        break