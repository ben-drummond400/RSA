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
p = 11177
q = 54323
 #p, q = generate_prime_number(16), generate_prime_number(16)

# 2. Find N = p * q

N = p * q

# 3. Find phi(N) = lcm(p - 1, q - 1)

phi = lcm((p - 1), (q - 1))

# 4. Choose the public key "e" such that 1 < e < phi(N),

e = generate_public_key(phi)

# 5. find the private key "d" such that e * d = 1 % phi(N)

d = generate_private_key(e, phi)
# correct for if d is negative
d = (d + phi) % phi

e = int(e)
d = int(d)
N = int(N)

m = input("enter number here")
m = int(m)
m = pow(m, e, N)
print("encrypted:", m)
h = pow(m, d, N)
print("decrypted:", h)
