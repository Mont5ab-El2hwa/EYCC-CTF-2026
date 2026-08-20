import hashlib
import os
import secrets

prime = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
g = (gx, gy)

def add(point1, point2):
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 and (y1 + y2) % prime == 0:
        return None
    if point1 == point2:
        slope = 3 * x1 * x1 * pow(2 * y1, -1, prime) % prime
    else:
        slope = (y2 - y1) * pow(x2 - x1, -1, prime) % prime
    x3 = (slope * slope - x1 - x2) % prime
    y3 = (slope * (x1 - x3) - y1) % prime
    return x3, y3

def mul(k, point):
    result = None
    current = point
    while k:
        if k & 1:
            result = add(result, current)
        current = add(current, current)
        k >>= 1
    return result

d = secrets.randbelow(n - 1) + 1
k = secrets.randbelow(n - 1) + 1
public = mul(d, g)
r = mul(k, g)[0] % n

print(f"qx = {public[0]}")
print(f"qy = {public[1]}")

while True:
    print("1. sign")
    print("2. flag")
    choice = input("> ")
    if choice == "1":
        message = input("message: ").encode()
        z = int.from_bytes(hashlib.sha256(message).digest(), "big") % n
        s = pow(k, -1, n) * (z + r * d) % n
        print(f"r = {r}")
        print(f"s = {s}")
    if choice == "2":
        key = int(input("key: "))
        if key == d:
            print(os.getenv("FLAG", "EYCC{local_flag}"))
        else:
            print("no")
        break
