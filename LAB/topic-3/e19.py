text = "ABCDABCABCDA"
pattern = "ABCDA"

for i in range(len(text) - len(pattern) + 1):
    print("Alignment", i)
    if text[i:i+len(pattern)] == pattern:
        print("Match at position", i)
    else:
        print("Mismatch")