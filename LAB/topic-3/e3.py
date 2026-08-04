arr = [10, 25, 15, 25, 30, 25, 40]
key = 25

for i in range(len(arr)):
    if arr[i] == key:
        print("First occurrence at position", i + 1)
        break