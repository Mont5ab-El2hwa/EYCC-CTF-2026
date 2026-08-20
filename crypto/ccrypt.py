import bcrypt
import hashlib
import os
import secrets
wew = b"life is great but ai is taking over my job but ig nth to do about it.."
alphabet = "0123456789abcdef"
tail = "".join(secrets.choice(alphabet) for _ in range(32)).encode()
password = wew + tail
answer = input("> ").encode()
while True:
    if bcrypt.checkpw(password, answer):
        print(os.getenv("FLAG", "EYCC{local_flag}"))
    else:
        print("no")