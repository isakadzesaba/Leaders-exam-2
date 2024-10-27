def factorial(num):
    if num == 0:
        return 1
    result = 1
    
    for i in range(1, num + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(0))