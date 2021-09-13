; Se dau 2 siruri de octeti S1 si S2 de aceeasi lungime. Sa se construiasca sirul D astfel incat fiecare element din D sa reprezinte maximul dintre elementele de pe pozitiile corespunzatoare din S1 si S2.
; exemplu:
; S1: 1, 3, 6, 2, 3, 7
; S2: 6, 3, 8, 1, 2, 5
; D: 6, 3, 8, 2, 3, 7

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 db 1, 3, 6, 2, 3, 7
    s2 db 6, 3, 8, 1, 2, 5
    ls equ $-s2 ; ambele siruri au aceeasi dimensiune deci voi declara lungimea ambelor folosind lungimea lui s2
    d times ls db 0

; our code starts here
segment code use32 class=code
    start:
        mov ecx, ls
        mov esi, 0
        repeta:
            mov al, [s1+esi]
            cmp al, [s2+esi]
            jge adauga_s1
            jmp adauga_s2
            adauga_s2:
                mov al, [s2+esi]
                mov [d+esi], al
                jmp final
            adauga_s1:
                mov [d+esi], al
            final:
                inc esi
        loop repeta
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
