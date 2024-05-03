from pwn import *
binary_path = './test.py'
p = remote('10.21.232.3', '2048')
#p = process(['python3',binary_path])

# Send inputs to the binary
#p.sendline(b'0x1272')
#p.sendline(b'0x74')
p.sendline(b'0x12f6')
p.sendline(b'0x74')
p.sendline(b'y')
#p.sendline(b'0x1278')
#p.sendline(b'0x0a')
#p.sendline(b'0x1277')
#p.sendline(b'0x2e')
p.sendline(b'0x12fc')
p.sendline(b'0x2d')
p.sendline(b'y')
p.sendline(b'0x12fb')
p.sendline(b'0x26')
# Receive output from the binary
output = p.recvall().decode('utf-8')

# Print the output
print(output)

# Close the connection
p.close()
