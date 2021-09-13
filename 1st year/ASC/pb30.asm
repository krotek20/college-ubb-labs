bits 32

global start, text, fmt

extern exit, scanf, printf, strlen, inverseaza
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll
import strlen msvcrt.dll

segment data use32 class=data
    text resb 100
    fmt db '%s', 0
    space db 10, 0
segment code use32 class=code
    start:
        .repeta:
            push dword text
            push dword fmt
            call [scanf]
            add esp, 8
            
            cmp eax, 0
            je final
            
            push dword text
            call [strlen]
            add esp, 4
            
            push eax
            call inverseaza
            
            push dword space
            push dword fmt
            call [printf]
            add esp, 8
            
            jmp .repeta
            
        
        final:
        
        
        push dword 0
        call [exit]