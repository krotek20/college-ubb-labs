bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 1, 2, 3
    ls equ $-s
    r times ls db 0
    k equ 3
    
; our code starts here
segment code use32 class=code
    start:
        mov bl, 0
        mov ecx, ls
        mov esi, 0
        repeta:
            mov al, [s+esi]
            add bl, al
            add al, k
            mov [r+esi], al
            add esi, 1
        loop repeta
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
