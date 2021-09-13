bits 32

global start        

extern exit, fopen, fclose, printf, fscanf, strlen
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fscanf msvcrt.dll
import strlen msvcrt.dll

segment data use32 class=data
    numeFis db 'fisier.txt', 0
    modacces db 'r', 0
    descriptor dd -1
    
    fmt db '%s ', 0
    fmt_char db '%c', 0
    cuv resb 100
    rez resd 100
    
    punct db '.', 0
    
segment code use32 class=code

    citeste_cuvant:
        ; fscanf(descriptor, format, var1...)
        push dword cuv
        push dword fmt
        push dword [descriptor]
        call [fscanf]
        add esp, 12
        ret

    verificare_punct:
        ; strlen(adr) -> eax = lungime cuvant
        push dword cuv
        call [strlen]
        add esp, 4
        
        cmp byte[cuv+eax-1], '.'
        je afiseaza_punct
        jmp afiseaza_normal
        
        afiseaza_punct:
            dec eax
            
            cmp eax, 0
            je done
            
            push eax
            
            mov ebx, 0
            mov bl, [cuv+eax-1]
            
            push ebx
            push dword fmt_char
            call [printf]
            add esp, 8
            pop eax
            jmp afiseaza_punct
            
        afiseaza_normal:
            push dword cuv
            push dword fmt
            call [printf]
            add esp, 8
            ret
            
        done:
            push dword punct
            push dword fmt
            call [printf]
            add esp, 8
            ret
            
    
    start:
        ; deschidere fisier
        push dword modacces
        push dword numeFis
        call [fopen]
        add esp, 8
        
        cmp eax, 0
        je final
        
        mov [descriptor], eax
        
        repeta:
            call citeste_cuvant
            cmp eax, 0
            jle final
            call verificare_punct
            jmp repeta
            
        final:
            
            push dword [descriptor]
            call [fclose]
            add esp, 4
            
        push    dword 0
        call    [exit]
