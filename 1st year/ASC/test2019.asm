bits 32

global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a1 db '256,-256'
    a2 dw 256, 256h
    a3 dw $-a2
    a4 equ -256/4
    a5 db 128>>1, 128<<1
    a6 dw a2-a5, ~(a2-a5)
    a8 dd 256h^256, 256256h
    
    a10 dw -255, 256
    a11 dw 256-256h
    a12 times 4 dw 256
    a14 dw -256
    a15 times 2 dd 12345678h
segment code use32 class=code
    start:
        
        push    dword 0
        call    [exit]
