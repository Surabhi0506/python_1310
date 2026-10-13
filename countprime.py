def countPrime(n):
    count = 0
    sum = 1
    for i in range(2, n+1):
        isPrime = True
        for j in range(2,i):
            if i%j==0:
                sum = n // j + sum 
                isPrime = False
                break

        if isPrime:
            count += 1
    return count