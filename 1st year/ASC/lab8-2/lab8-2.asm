; sir de dublucuvinte. Sa se puna intr-un sir de octeti, octetii cuv sup care sunt impari si se regasesc in [a,b]
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 12345678h, 1A2B3C4Dh, 0FE98DC76h
    ls equ ($-s)/4
    d times ls db 0
    a db 10
    b db 100
    doi db 2
    i dd 0

; our code starts here
segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        mov esi, s
        mov edi, 0
        cld
        repeta:
            lodsw
            lodsw
            mov bh, ah ; octetul superior
            mov bl, al ; octetul inferior
            
            mov ah, 0
            div byte[doi]
            cmp ah, 1
            je adauga1
            
            next1:
            mov al, bh
            mov ah, 0
            div byte[doi]
            cmp ah, 1
            je adauga2
            
            next2:
            inc dword[i]
            cmp dword[i], ls
            je final
            jmp repeta
            
        adauga1:
            cmp bl, [a]
            jae adauga12
            jmp next1
            adauga12:
                cmp bl, [b]
                jbe adauga13
                jmp next1
                adauga13:
                    mov [d+edi], bl
                    inc edi
                    jmp next1
        
        adauga2:
            cmp bh, [a]
            jae adauga22
            jmp next2
            adauga22:
                cmp bh, [b]
                jbe adauga23
                jmp next2
                adauga23:
                    mov [d+edi], bh
                    inc edi
                    jmp next2
        
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
