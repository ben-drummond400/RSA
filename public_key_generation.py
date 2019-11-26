from random import randrange
from numpy import gcd


def is_coprime(e, phi):
    if gcd(e, phi) == 1:
        return True
    else:
        return False


def generate_public_candidate(phi):
    e = randrange(1, phi)
    return e


def generate_public_key(phi):

    e = generate_public_candidate(phi)

    while not is_coprime(e, phi):
        e = generate_public_candidate(phi)
    return e

