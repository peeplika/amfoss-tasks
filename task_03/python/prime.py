n = int(input("Enter a positive number: "))

if n < 0:
    print("Not valid")
else:
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    print("Prime numbers up to", n, "are:", primes)

