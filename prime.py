def isPrime(n):
    sum = 1
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            sum = n // i + sum
            return False

    return True