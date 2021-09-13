; 4. Se da octetul A. Sa se obtina numarul intreg n reprezentat de bitii 2-4 ai lui A. Sa se obtina apoi in B octetul rezultat prin rotirea spre dreapta a lui A cu n pozitii. Sa se obtina dublucuvantul C:
; bitii 8-15 ai lui C sunt 0
; bitii 16-23 ai lui C coincid cu bitii lui B
; bitii 24-31 ai lui C coincid cu bitii lui A
; bitii 0-7 ai lui C sunt 1
; a,b - byte , c - dword

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 54 ; va fi 0  0  1  1  0  1  1  0  b si 16h (am pus spatiere pentru a putea numerota pozitiile mai jos)
            ;       a7 a6 a5 a4 a3 a2 a1 a0
    b db 0
    n db 0
    c dd 0

; our code starts here
segment code use32 class=code
    start:
        mov al, [a]
        mov cl, 2
        shr al, cl ; al = 00a7a6a5a4a3a2b = 00001101b
        and al, 00000111b ; al = 00000a4a3a2b = 00000101b
        or byte[n], al ; n = 00000101b = 5 = 5h
        mov al, [a]
        mov byte[b], al
        mov cl, [n]
        ror byte[b], cl ; b = a4a3a2a1a0a7a6a5 = 10110001b = 177 = B1h
        ; al = [a] = 00110110b
        mov byte[c+3], al ; bitii 24-31 ai lui C coincid cu bitii lui A
        mov al, byte[b]
        mov byte[c+2], al ; bitii 16-23 ai lui C coincid cu bitii lui B
        mov byte[c+1], 0 ; bitii 8-15 ai lui C sunt 0
        mov byte[c+0], 0ffh ; bitii 0-7 ai lui C sunt 1
        ; astfel c = a7...a0b7...b00000000011111111b
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
