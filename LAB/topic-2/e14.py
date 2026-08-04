def insertion_sort_count_shifts(a):
    s = 0
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            s += 1
            j -= 1
        a[j + 1] = key
    return a, s

log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0]
print(insertion_sort_count_shifts(log))