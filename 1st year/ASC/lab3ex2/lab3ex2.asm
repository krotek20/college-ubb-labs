; problema 7
; (a-2)/(b+c)+a*c+e-x
; a,b-byte; c-word; e-doubleword; x-qword
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 18
    b db -2
    c dw 18
    e dd 12
    x dq 8

; our code starts here
segment code use32 class=code
    start:
        mov eax, 0
        mov al, byte[a]
        sub al, 2
        cbw
        cwd ; dx:ax = a-2
        mov cx, dx
        mov bx, ax
        mov al, byte[b]
        cbw
        add ax, word[c]
        mov dx, cx
        mov cx, ax
        mov ax, bx
        idiv cx ; (a-2)/(b+c) -> cat - ax, rest - dx
        mov cx, dx
        mov bx, ax ; cx:bx = cat, rest
        mov al, byte[a]
        cbw
        imul word[c] ; dx:ax = a*c
        add ax, bx
        adc dx, 0 ; dx:ax = (a-2)/(b+c)+a*c
        push dx
        push ax
        pop eax
        add eax, dword[e] ; eax = (a-2)/(b+c)+a*c+e
        cdq
        sub eax, dword[x+0]
        sbb edx, dword[x+4] ; edx:eax = (a-2)/(b+c)+a*c+e-x
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
