bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 00001111b
    b dw 00000000111111111b
    c dw 0

; our code starts here
segment code use32 class=code
    start:
        mov ax, word[b]
        mov [c], ax
        shl word[c], 8 ; C high completat
        mov ax, word[c]
        and al, 00000000b
        or al, 00000110b
        mov byte[c], al
        mov bx, word[b]
        mov cl, 3
        shr bx, cl ; bx = 000b15...b8b7...b3
        and bl, 00111000b ; bl = 00b8b7b6000
        or byte[c], bl
        mov al, byte[a]
        shl al, 4 ; al = a3a2a1a00000
        and al, 11000000b ; al = a3a2000000
        not al ; (not)a3(not)a2111111
        and al, 11000000b
        or byte[c], al
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
