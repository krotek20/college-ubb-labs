; exercitiu suplimentar: Identificarea numerelor prime dintr-un sir de octeti si mutarea lor in alt sir de octeti
; exemplu:
; s db 1, 2, 3, 6, 11, 15
; d db 2, 3, 11 (sir rezultat)

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 1, 2, 3, 6, 11, 15
    ls equ $-s
    d times ls db 0
    aux db 0

; our code starts here
segment code use32 class=code
    start:
        mov esi, s
        mov edi, d
        mov ecx, ls
        cld
        repeta:
            lodsb
            cmp al, 0
            je final
            
            cmp al, 1
            je final
            
            cmp al, 2
            je adauga
            
            mov byte[aux], al
            mov bl, 2
            verifica_prim:
                mov al, byte[aux]
                cbw
                
                div bl
                cmp ah, 0
                je final
                
                add bl, 1
                mov al, byte[aux]
                cmp bl, al
                je adauga
                jmp verifica_prim
                
            adauga:
                stosb
            final:
            
        loop repeta
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
