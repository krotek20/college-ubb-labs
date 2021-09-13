bits 32

global start        

extern exit, scanf, fopen, fclose, fprintf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    nume_fisier db 'piramida.txt',0
    mod_acces_read db 'r', 0
    mod_acces_write db 'w', 0
    descriptor dd -1
    
    nr dd 0
    nr_fmt db '%d', 0
    nr_fmt_space db '%2d', 0
    fail db 'fail', 0
    fmt_fail db '%s', 0
    
segment code use32 class=code
    citeste_numere:
        ; scanf(format, var...)
        push dword nr
        push dword nr_fmt
        call [scanf]
        add esp, 8
        ret
        
    scrie_in_fisier:
        ; fprintf(descriptor, format, var...)
        push dword [nr]
        push dword nr_fmt_space
        push dword [descriptor]
        call [fprintf]
        add esp, 12
        ret
        
    start:
        push dword mod_acces_write
        push dword nume_fisier
        call [fopen]
        add esp, 8
        
        cmp eax, 0
        je final
        mov [descriptor], eax
        mov ecx, 0
        
        repeta:
            push ecx
            mov dword[nr], 0
            call citeste_numere
            cmp dword[nr], 0
            je next
            call scrie_in_fisier
            pop ecx
            inc ecx
            jmp repeta
        
        next:
        
        
        
        final:
        push    dword 0
        call    [exit]
