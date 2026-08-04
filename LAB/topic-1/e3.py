# Iterative
def fact_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive
def fact_rec(n):
    return 1 if n <= 1 else n * fact_rec(n - 1)

# Test
n = 5
print(f"Iterative: {fact_iter(n)}")
print(f"Recursive: {fact_rec(n)}")

# Performance comparison
import time

def time_func(func, n):
    start = time.time()
    func(n)
    return (time.time() - start) * 1e6

print(f"\nPerformance (microseconds):")
print(f"Iterative: {time_func(fact_iter, 100):.2f} μs")
print(f"Recursive: {time_func(fact_rec, 100):.2f} μs")