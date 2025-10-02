from concurrent.futures import ProcessPoolExecutor
import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primes_count(nums):
    with ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, nums)
    return sum(results)


if __name__ == "__main__":
    assert primes_count([2, 3, 4, 5, 15, 17, 19]) == 5
    print("Test passed")
