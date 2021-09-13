bits 32

global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data

segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        mov al, 147
        mov bl, 113
        add al, bl
        push    dword 0
        call    [exit]
