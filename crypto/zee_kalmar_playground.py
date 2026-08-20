import hashlib
import os
import secrets

p = 74798904015587536914342671090570976685017599475037092903418312313406430268579
q = 37399452007793768457171335545285488342508799737518546451709156156703215134289
g = 4
x = secrets.randbelow(q - 1) + 1
y = pow(g, x, p)
offset = 1337
target = y * pow(g, offset, p) % p
k = secrets.randbelow(q - 1) + 1
t = pow(g, k, p)
e = int.from_bytes(hashlib.sha256(str(t).encode()).digest(), "big") % q
s = (k + e * x) % q

print(f"y = {y}")
print(f"target = {target}")
print(f"t = {t}")
print(f"s = {s}")

t2 = int(input("t: "))
s2 = int(input("s: "))
e2 = int.from_bytes(hashlib.sha256(str(t2).encode()).digest(), "big") % q

if pow(g, s2, p) == t2 * pow(target, e2, p) % p:
    print(os.getenv("FLAG", "EYCC{local_flag}"))
else:
    print("skill issue!")
