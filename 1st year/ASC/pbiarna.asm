bits 32 

global start 

extern exit, scanf
import exit msvcrt.dll
import scanf msvcrt.dll

segment data use 32 class=data
    nr_elem dd 0
    suma dd 0
    sir resd 10
    format_nr db "%d", 0
    sir_sume resb 10
    zece dd 10
    
segment code use 32 class=code
    start:
        mov ax, -10010100b
        mov ebx,0
        ;citim numarul de elemente din sir
        push dword nr_elem
        push dword format_nr
        call [scanf]
        add esp,8
        
        mov ecx,[nr_elem]
        mov esi,sir
        repeta:
            push ecx
            push dword esi
            push dword format_nr
            call [scanf]
            add esp,8
            inc ebx
            add esi,4
            pop ecx
        loop repeta
        
        mov ecx,ebx
        mov esi,sir
        mov edi,sir_sume
        
        repeta2:
            lodsd
            mov dword[suma],0
            cifra:
                mov edx,0
                div dword[zece]
                test edx,1
                jnz impar
                add [suma],edx
                impar:
                cmp eax,0
            jne cifra
            mov al,[suma]
            stosb
        loop repeta2
        
        push dword 0
        call exit