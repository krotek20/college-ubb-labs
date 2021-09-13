; sd - sir de dword

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    sd dd 12345678h, 1A2B3C4Dh, 11223344h
    lensd equ ($-sd)/4
    a times lensd db 0
    b times lensd db 0

; our code starts here
segment code use32 class=code
    start:
        mov esi, 2 ; pentru a
        mov edi, 1 ; pentru b
        mov ebp, 0 ; pentru sd
        mov ecx, lensd
        repeta:
            mov al, byte[sd+esi]
            mov [a+ebp], al
            mov al, byte[sd+edi]
            mov [b+ebp], al
            add esi, 4
            add edi, 4
            add ebp, 1
        loop repeta

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
