bits 32

global inverseaza
extern text, fmt, printf
import printf msvcrt.dll

segment code use32 class=code
    inverseaza:
        pop esi
        mov eax, 0
        
        .invert:
            mov al, [text+esi]
            
            push dword eax
            push dword fmt
            call [printf]
            add esp, 8
            
            cmp esi, 0
            je .return
            
            dec esi
            jmp .invert
        
        .return:
        ret