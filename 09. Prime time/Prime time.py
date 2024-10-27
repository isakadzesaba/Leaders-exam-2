def prime_num(n):
    primes = []
    
    for i in range(2, n + 1):
        prime = True  
        for i in range(2, i):
            if i % i == 0:
                prime = False
                break
        if prime:  
            primes.append(i)
    return primes

print(prime_num(11))