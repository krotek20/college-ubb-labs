; (b/a*2+10)*b-b*5+c
; a - byte, b = word, c = qw
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 2
    b dw -10
    c dq -160

; our code starts here
segment code use32 class=code
    start:
        mov ax, [b]
        div byte[a] ; al - cat, ah - rest
        mov bl, 2
        mul bl ; ax = b/a*2
        add ax, 10 ; ax = b/a*2+10
        mul word[b] ; dx:ax = (b/a*2+10)*b
        mov cx, dx
        mov bx, ax
        mov ax, 5
        mul word[b] ; dx:ax = b*5
        sub bx, ax
        sbb cx, dx ; cx:bx = rez
        push cx
        push bx
        pop eax
        cdq ; edx:eax = rez
        add eax, [c+0]
        adc edx, [c+4] ; edx:eax = rez
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
