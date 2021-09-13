bits 32

global start        

extern exit, fopen, fscanf, printf, fclose, scanf, strlen
import exit msvcrt.dll
import fopen msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll
import strlen msvcrt.dll

segment data use32 class=data
    num_fis db 'cuvinte.txt', 0
    mod_acces db 'r', 0
    descriptor dd -1
    
    cuv times 100 db 0
    L dd 0
    contor dd 0
    
    nr_fmt db '%d', 0
    cuv_fmt db '%s', 0
    
segment code use32 class=code
    start:
        push dword mod_acces
        push dword num_fis
        call [fopen]
        add esp, 8
        
        cmp eax, 0
        je final
        
        mov [descriptor], eax
        
        push dword L
        push dword nr_fmt
        call [scanf]
        add esp, 8
        
        cmp dword[L], 0
        jle final
        
        repeta:
            push dword cuv
            push dword cuv_fmt
            push dword [descriptor]
            call [fscanf]
            add esp, 12
            
            cmp eax, 0
            jle afisare
            
            push dword cuv
            call [strlen]
            add esp, 4

            cmp eax, dword[L]
            jl repeta
            
            inc dword[contor]
            jmp repeta
        
        afisare:
            push dword [contor]
            push dword nr_fmt
            call [printf]
            add esp, 8
            
        push dword [descriptor]
        call [fclose]
        add esp, 4

        final:
        push    dword 0
        call    [exit]
