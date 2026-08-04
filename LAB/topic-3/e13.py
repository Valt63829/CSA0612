text = "MISSISSIPPI"
pattern = "ISSI"

for i in range(len(text) - len(pattern) + 1):
    c = 0
    while c < len(pattern) and text[i + c] == pattern[c]:
        c += 1

    print("Shift", i, "| Comparisons =", c + 1 if c < len(pattern) else c,
          "|", "Match" if c == len(pattern) else "Mismatch")