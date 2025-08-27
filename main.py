import math

def isPrime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
        
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

print(f"É 7 um número primo? {isPrime(7)}")
print(f"É 1 um número primo? {isPrime(24)}")