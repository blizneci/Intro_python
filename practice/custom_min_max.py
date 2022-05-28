import timeit


def are_coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

print(
    min(
            timeit.repeat(
                stmt="[i ** 2 for i in range(100)]",
                number=1000,
                repeat=3
                )
            )
        )

print(
    min(
            timeit.repeat(
                stmt="list(map(lambda i: i ** 2, range(100)))",
                number=1000,
                repeat=3
                )
            )
        )
