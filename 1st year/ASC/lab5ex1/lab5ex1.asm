; problema 24
; Se dau 2 siruri de octeti A si B. Sa se construiasca sirul R care sa contina elementele lui B in ordine inversa urmate de elementele in ordine inversa ale lui A.
; Exemplu:
; A: 2, 1, -3, 0
; B: 4, 5, 7, 6, 2, 1
; R: 1, 2, 6, 7, 5, 4, 0, -3, 1, 2

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 2, 1
    la equ $-a
    b db 4, 5, 7
    lb equ $-b
    r times la+lb db 0

; our code starts here
segment code use32 class=code
    start:
        mov ecx, lb
        mov esi, lb-1
        mov edi, 0
        
        repetaPentruB:
            mov al, [b+esi]
            mov [r+edi], al
            add edi, 1
            sub esi, 1
        loop repetaPentruB
        
        mov esi, la-1
        mov ecx, la
        
        repetaPentruA:
            mov al, [a+esi]
            mov [r+edi], al
            add edi, 1
            sub esi, 1
        loop repetaPentruA
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
