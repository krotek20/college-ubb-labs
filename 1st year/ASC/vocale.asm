bits 32

global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    fmt db '%c', 0
    fmt_afis db '%c',10,0
    vocale db 'a','e','i','o','u', 0
    len equ $-vocale
    litera resb 1
    
segment code use32 class=code
    verifica_vocala:
        mov al, [vocale+esi]
        cmp [litera], al
        je afiseaza
        ret
        
        afiseaza:
            push dword [litera]
            push dword fmt_afis
            call [printf]
            add esp, 8
            ret
    
    start:
        repeta:
            push dword litera
            push dword fmt
            call [scanf]
            add esp, 8
            
            cmp byte[litera], 0Ah
            je final
            
            mov esi, 0
            verif:
                call verifica_vocala
                inc esi
                cmp esi, len
                jb verif
            jmp repeta
            
            
        final:
        push    dword 0
        call    [exit]
