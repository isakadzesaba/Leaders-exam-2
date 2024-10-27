def binary_decimal(b):
    decimal = 0
    p = 0
    for i in reversed(b):
        decimal += int(i) * (2 ** p)
        p += 1

    return decimal

print(binary_decimal("10001"))
print(binary_decimal("1111"))