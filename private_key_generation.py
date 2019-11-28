from numpy import *


def generate_private_key_array(e, phi):
    a = phi
    b = e
    c = a % b
    count = 1

    while c > 0:
        a = long(b)
        b = long(c)
        c = long(a % b)
        count += 1
    data = zeros(count - 1)
    return data


def generate_private_key(e, phi):
    data = array(generate_private_key_array(e, phi), dtype=object)
    a = phi
    b = e
    c = a % b
    count = 0

    for i in range(0, len(data)):
        data[i] = -floor(a / b)
        a = b
        b = c
        c = a % b

    x = 1
    y = data[len(data) - 1]

    for i in range(len(data) - 1, 0, -1):
        if y == -1:
            y = long(data[i - 1] - x)
            x = 1
            count += 1
        elif y != -1:
            xo = long(x)
            x = long(y)
            y = long(y * data[i - 1] + xo)

    if count % 2 == 1:
        y *= -1

    return y
