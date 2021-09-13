bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    sw dw 26, 13, 3, 6, 7, 61
    lensw equ ($-sw)/2
    c db 0
    n times lensw db 0
    s db 7

; our code starts here
segment code use32 class=code
    start:
        mov esi, 0
        mov ecx, lensw
        repeta:
            mov al, byte[sw+esi]
            cbw
            mov bl, 3
            idiv bl
            cmp ah, 0
            je divizibil
            jmp final
            divizibil:
                add byte[c], 1
            final:
                add esi, 2
        loop repeta
        
        mov ecx, lensw
        mov esi, 0
        mov edi, 0
        repeta2:
            mov dl, 0
            mov ax, [sw+esi]
            mov bl, 10
            ultimaCifra:
                div bl
                add dl, ah
                cmp al, 0
                cbw
                jne ultimaCifra
            cmp dl, [s]
            jne final2
            mov ax, [sw+esi]
            mov [n+edi], ax
            add edi, 2
            final2:
                add esi, 2
        loop repeta2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
