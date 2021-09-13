bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern printf
import printf msvcrt.dll
extern scanf
import scanf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    mesaja db 'Introduceti a= ', 0
    mesajb db 'Introduceti b= ', 0
    formatcitire db '%d', 0
    mesajk db 'Valoarea constantei k este %d sau %x. ', 0
    mesajrez db 'Suma dintre %d si %d este %d si diferenta dintre %x si %x este %x', 0
    a dd 0
    b dd 0
    suma dd 0
    dif dd 0
    k equ 11
    
; our code starts here
segment code use32 class=code
    start:
        push dword mesaja
        call [printf]
        add esp, 4*1
        
        push dword a
        push dword formatcitire
        call [scanf]
        add esp, 4*2
        
        push dword mesajb
        call [printf]
        add esp, 4*1
        
        push dword b
        push dword formatcitire
        call [scanf]
        add esp, 4*2
        
        push dword k
        push dword k
        push dword mesajk
        call [printf]
        add esp, 4*3
        
        mov eax, [a]
        add eax, [b]
        mov [suma], eax
        
        sub eax, k
        mov [dif], eax
        
        push dword [dif]
        push dword k
        push dword [suma]
        push dword [suma]
        push dword [b]
        push dword [a]
        push dword mesajrez
        call [printf]
        add esp, 4*7
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
