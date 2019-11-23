from numpy import *
import random as rdm
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

p = 7411
q = 7717

# 2. Find N = p * q

N = p * q

# 3. Find phi(N) = lcm(p - 1, q - 1)
# since low values of e are less secure let pi = phi/2
# and find e in the interval (pi, phi)
phi = lcm((p - 1), (q - 1))
pi = int(phi/2)
# 4. Choose the public key "e" such that 1 < e < phi(N),
#       and gcd(e, phi(N)) == 1
# find all possible values of e and choose random
E = []
for i in range(pi, phi):
    if gcd(i, phi) == 1:
        E.append(i)
e = rdm.choice(E)


# determine the size of the euclidean algorithm matrix
count = 1
a = phi
b = e
c = a % b

while c > 0:
    a = b
    b = c
    c = a % b
    count += 1
data = zeros((count - 1, count + 1))

# 5. find the private key "d" such that e * d = 1 % phi(N)
#    (use euclidean algorithm to calculate modular multiplicative inverse)
a = phi
b = e
c = a % b


print(data)
# this method can be changed to be more efficient
for i in range(0, count - 1):
    data[i, i] = 1
    data[i, i + 1] = -floor(a / b)
    data[i, i + 2] = -1

    a = b
    b = c
    c = a % b

for i in range(count - 2, 0, -1):
    if data[i, i + 1] == data[i - 1, i + 1]:
        data[i - 1] -= data[i]
    elif data[i, i + 1] != data[i - 1, i + 1]:
        data[i - 1] *= data[i, i + 1]
        data[i - 1] += data[i]


x = data[0]
d = x[1]

# correct for if d is negative
check = x[count]
if check > 0:
    d *= -1
d = (phi + d) % phi


# set all values to integers
e = int(e)
d = int(d)
N = int(N)


m = input("enter number here")
m = int(m)
m = pow(m, e, N)
print("encrypted:", m)
h = pow(m, d, N)
print("decrypted:", h)
