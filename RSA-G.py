from numpy import *
from prime_numbers import generate_prime_number
from public_key_generation import generate_public_key
from private_key_generation import generate_private_key
"""
1. Choose two prime numbers p and q
2. Find N = p * q 
3. Find phi(N) = lcm(p - 1, q - 1)
4. Choose the public key "e" such that 1 < e < phi(N),
    and gcd(e, phi(N)) == 1
5. find d such that e * d = 1 % phi(N)
    (use euclidean algorithm to calculate modular multiplicative inverse)

n ^ e % N = m (our encrypted number)
m ^ d % N = n (our original number)

"""

# 1. Choose two prime numbers p and q
p = 602482819
q = 1408263589
# p, q = generate_prime_number(128), generate_prime_number(128)

# 2. Find N = p * q

N = p * q
print("N", N)

# 3. Find phi(N) = lcm(p - 1, q - 1)
# since low values of e are less secure let pi = phi/2
# and find e in the interval (pi, phi)
phi = lcm((p - 1), (q - 1))
print("phi", phi)
# 4. Choose the public key "e" such that 1 < e < phi(N),
#       and gcd(e, phi(N)) == 1
# find all possible values of e and choose random
e = generate_public_key(phi)
# e = 65537
print("e", e)



# 5. find the private key "d" such that e * d = 1 % phi(N)
#    (use euclidean algorithm to calculate modular multiplicative inverse)
d = generate_private_key(e, phi)
# correct for if d is negative
d = (d + phi) % phi
print(d)
# set all values to integers
e = int(e)
d = int(d)
N = int(N)
print("prod", (e * d) % phi)
# m = input("enter number here")
m = 6000
m = 2**e % N
print("encrypted:", m)
h = m**d % N
print("decrypted:", h)
