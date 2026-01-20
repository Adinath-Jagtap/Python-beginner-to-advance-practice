# 2) Check if a number is prime — efficient sqrt(n) check
import math

def is_prime(n: int) -> bool:
    """
    Return True if n is prime, False otherwise.
    Handles n <= 1 as non-prime. Uses trial division up to sqrt(n).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # test odd divisors from 3 to sqrt(n)
    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

# Examples
for x in [1, 2, 3, 4, 17, 18, 97]:
    print(x, "is prime?", is_prime(x))