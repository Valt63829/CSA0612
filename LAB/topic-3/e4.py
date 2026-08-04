arr = [7, 12, 7, 25, 18, 7, 30, 7]
key = 7

count = 0
print("Occurrences at positions:")
for i in range(len(arr)):
    if arr[i] == key:
        print(i + 1, end=" ")
        count += 1

print("\nTotal occurrences =", count)