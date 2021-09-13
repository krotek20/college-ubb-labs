bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 3
    b db 5
    c dw 2
    d dd 10
    x dq 20
    ; aux resb 1
    ; aux resw 1
    ; aux resd 1
; our code starts here
segment code use32 class=code
    start:
        mov al, [b]
        cbw
        imul word[a] ; -> dx:ax
        mov bx, ax
        mov cx, dx ; cx:bx = a*b
        mov al, [b]
        cbw
        cwd
        idiv word[c] ; ax - cat, dx - rest -> 
        cwd
        add ax, bx
        adc dx, cx ; a*b+b/c -> dx:ax
        sub ax, 1
        sbb dx, 0 ; (a*b+b/c-1) -> dx:ax
        push dx
        push ax
        pop ebx
        mov al, [b]
        cbw
        add ax, [c] ; b+c -> ax
        mov cx, ax
        push ebx
        pop ax
        pop dx
        idiv cx ; (a*b+b/c-1)/(b+c) -> dx:ax, ax - cat, dx - rest
        cwde
        add eax, [d]
        cdq ; edx:eax
        mov ebx, dword[x+0]
        mov ecx, dword[x+4]
        sub eax, ebx
        sbb edx, ecx ; rez -> edx:eax
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
