def decimal_binary(d):
    if d == 0:
        return "0"
    b = ""

    while d > 0:
        rem = d % 2
        b += str(rem)
        d //= 2
    return b

print(decimal_binary(17))
print(decimal_binary(15))
print(decimal_binary(0))