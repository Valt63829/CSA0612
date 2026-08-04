text = "PROGRAMMINGLAB"

for pattern in ["LAB", "TEST"]:
    count = 0
    found = False

    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while j < len(pattern):
            count += 1
            if text[i+j] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            found = True
            break

    print(pattern, "->", "Found" if found else "Not Found")
    print("Comparisons =", count)