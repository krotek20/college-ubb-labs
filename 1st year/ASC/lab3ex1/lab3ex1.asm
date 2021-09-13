; problema 7
; (c+c+c)-b+(d-a)
; a - byte, b - word, c - double word, d - qword - Interpretare cu semn
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 5
    b dw 3
    c dd 2
    d dq 7
    
; our code starts here
segment code use32 class=code
    start:
        mov eax, 0
        mov eax, [c]
        add eax, [c]
        add eax, [c] ; eax = c+c+c
        mov ebx, eax
        mov ax, [b]
        cwde
        sub ebx, eax ; ebx = (c+c+c)-b
        mov al, [a]
        cbw
        cwde
        cdq ; edx:eax
        sub dword[d+0], eax
        sbb dword[d+4], edx
        mov eax, ebx
        cdq
        add eax, dword[d+0]
        adc edx, dword[d+4] ; edx:eax = (c+c+c)-b+(d-a)
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
