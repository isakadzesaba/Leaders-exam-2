def fibonacci(s):
    if s <= 0:
        return []
    elif s == 1:
        return [0]
    
    n = [0,1]
    
    for i in range(2, s):
        num = n[i - 1] + n[i - 2]
        n.append(num)
    return n

print(fibonacci(5))
print(fibonacci(7))