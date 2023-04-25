from pwn import *
import hashlib

m = hashlib.sha1()
m.update(b"Hello")
d = m.digest()

print(d)

# p = process("/home/sandip/Desktop/test/main")
p = remote("m1", 1111)
p.send(d)
print(p.recvuntil(': '))

p.send("Hello")
p.interactive()
