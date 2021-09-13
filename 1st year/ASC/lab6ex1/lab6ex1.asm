; Se da un sir de caractere S. Sa se construiasca sirul D care sa contina toate literele mici din sirul S.
; exemplu:
; S: 'a', 'A', 'b', 'B', '2', '%', 'x'
; D: 'a', 'b', 'x'
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 'a', 'A', 'b', '2', '%', 'x'
    ls equ ($-s)
    d times ls db 0

; our code starts here
segment code use32 class=code
    start:
        mov ecx, ls
        mov esi, 0
        mov edi, 0
        repeta:
            mov al, [s+esi]
            cmp al, 'a'
            jl not_lower
            cmp al, 'z'
            jg not_lower
            mov [d+edi], al
            inc edi
            not_lower:
            inc esi  
        loop repeta
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
