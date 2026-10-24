"""[LEARNING LOGS] isPrime_large"""
num = int(input())

def is_prime(n):
    """Find the prime number"""
    if n <= 1:
      return False
    
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
          return False 
    return True
if is_prime(num):
    print("YES")
else:
    print("NO")
