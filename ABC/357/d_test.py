def efficient_calculation(n, digit):
    # Compute 10^digit - 1
    base = pow(10, digit) - 1

    # If base is 0, handle edge case
    if base == 0:
        return n

    # Compute (10^(digit * n) - 1) // (10^digit - 1)
    result = n * (pow(10, digit * n, base * n) - 1) // base

    return result


# Example usage:
n = 3
digit = 2
print(efficient_calculation(n, digit))
