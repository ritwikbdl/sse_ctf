import random


def encrypt(plaintext, key):
    ciphertext = b""
    plaintext_block = [plaintext[i : i + 16] for i in range(0, len(plaintext), 16)]
    for c in plaintext_block:
        ciphertext += bytes([c[i] ^ key[i] for i in range(16)])

    return ciphertext


with open("bin", "rb") as f:
    bin_ = f.read()
    key = random.randbytes(16)
    bin_out = encrypt(bin_, key)

with open("bin_out", "wb") as fo:
    fo.write(bin_out)
