text = "DataStructuresAndAlgorithms".lower()
pattern = "ALGORITHMS".lower()

for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print("Pattern found at position", i)
        break