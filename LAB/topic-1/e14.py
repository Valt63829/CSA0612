# Experiment 14: Exponentiation
# Compare Iterative Method and Recursive Fast Power

# -------------------------------
# Iterative Method - O(n)
# -------------------------------
def iterative_power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


# -------------------------------
# Recursive Fast Power - O(log n)
# -------------------------------
def fast_power(x, n):
    if n == 0:
        return 1

    half = fast_power(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# -------------------------------
# Main Program
# -------------------------------
x = 2
n = 10

print("Base (x):", x)
print("Exponent (n):", n)
print("Iterative Power:", iterative_power(x, n))
print("Recursive Fast Power:", fast_power(x, n))