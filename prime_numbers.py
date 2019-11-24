from random import randrange, getrandbits


def sieveOfEratosthenes(n):
    # Sieving for large primes, is hopeless
    ''' Get all primes up to n, assume all prime, from 2 iteratively flag every prime's multiples as not prime. 
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'''

    prime = [True for i in range(n+1)]
    i = 2

    while i*i <= n:
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False
        i += 1

    prime[0] = prime[1] = False
    return [i for i, isPrime in enumerate(prime) if isPrime]


def sieveOfAtkin(n):
    # Sieving for large primes, is hopeless
    '''Get all primes up to n, worst case O(n) faster the Eratosthenes. https://en.wikipedia.org/wiki/Sieve_of_Atkin.'''

    sieve = [False for i in range(n+1)]

    x = 1
    while x*x < n:
        y = 1
        while y*y < n:
            i = (4*x*x) + (y*y)

            if i <= n and (i % 12 == 1 or i % 12 == 5):
                sieve[i] = True

            i = (3 * x * x) + (y * y)
            if i <= n and i % 12 == 7:
                sieve[i] = True

            i = (3 * x * x) - (y * y)
            if x > y and i <= n and i % 12 == 11:
                sieve[i] = True
            print(i)

            y += 1
        x += 1

    r = 5
    while r * r < n:
        if sieve[r]:
            for i in range(r * r, n, r * r):
                sieve[i] = False
        r += 1

    return [i for i, isPrime in enumerate(sieve) if isPrime]


# https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb


def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


if __name__ == '__main__':
    # n = 2 ** 128
    # print([prime for prime in sieveOfAtkin(n)])
    print(generate_prime_number(length=2046))
