arr = [14, 9, 22, 35, 18, 41, 27]
key = 18

# Ordinary Search
count = 0
for i in range(len(arr)):
    count += 1
    if arr[i] == key:
        print("Ordinary Search: Found at position", i + 1)
        print("Comparisons =", count)
        break

# Sentinel Search
a = arr[:]
a.append(key)
i = 0
while a[i] != key:
    i += 1

if i < len(arr):
    print("Sentinel Search: Found at position", i + 1)