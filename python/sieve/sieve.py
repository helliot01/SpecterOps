from math import log, ceil
class Sieve:
    def __init__(self) -> None:
        pass

    def nth_prime(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be greater than 0")
        if n < 6:
            limit = 12
        else:
            limit  = ceil(n*log(n*log(n)))
        while True:
            primes = list(self.primes_up_to(limit))
            if len(primes) > n:
                return primes[n]
            limit *= 2

    def primes_up_to(self, limit):
        prime = [True] * limit
        for i in range(2, limit):
            if(prime[i]):
                yield i
                for c in range(i*i, limit, i):
                    prime[c] = False