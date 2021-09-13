; Se da un fisier text. Sa se citeasca continutul fisierului, sa se contorizeze numarul de consoane si sa se afiseze aceasta valoare. Numele fisierului text este definit in segmentul de date.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern fopen, fclose, fread, printf
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll   
import printf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    numfisier db 'fisier.txt', 0
    modacces db 'r', 0
    descriptor dd -1
    len equ 100
    a times len db 0
    format db "Am citit %d consoane din fisier", 0
    contor dd 0

; our code starts here
segment code use32 class=code
    start:
        ; deschidere fisier
        push dword modacces
        push dword numfisier
        call [fopen]
        add esp, 4*2
        
        ; verificam daca s-a deschis fisierul
        cmp eax, 0
        je final
        
        mov [descriptor], eax
        
        ; citirea a maxim 100 de caractere
        push dword [descriptor]
        push dword len
        push dword 1
        push dword a
        call [fread]
        add esp, 4*4
        
        mov ebx, eax
        mov ecx, eax
        consoane:
            mov esi, a
            add esi, dword[contor]
            inc dword[contor]
            lodsb
            cmp dword[contor], ebx
            je final
            
            cmp    al, 'A'
            jae    pas1
            jmp    decrement
            pas1:
                cmp    al, 'Z'
                jbe    verificaLitera
            cmp    al, 'z'
            jbe    pas2
            jmp    decrement
            pas2:
                cmp    al, 'a'
                jae    verificaLitera
            jmp    decrement
            
            verificaLitera:
                cmp    al, 'a'     
                je     decrement
                cmp    al, 'e'     
                je     decrement
                cmp    al, 'i'     
                je     decrement
                cmp    al, 'o'     
                je     decrement
                cmp    al, 'u'     
                je     decrement
                cmp    al, 'A'     
                je     decrement
                cmp    al, 'E'     
                je     decrement
                cmp    al, 'I'     
                je     decrement
                cmp    al, 'O'     
                je     decrement
                cmp    al, 'U'     
                je     decrement
                jmp    consoane
        decrement:
            dec ecx 
            jmp    consoane
            
        final:
            ; afisam numarul de consoane citite
            ; printf(format, eax, text)
            push dword ecx
            push dword format
            call [printf]
            add esp, 4*3
            
            push dword [descriptor]
            call [fclose]
            add esp, 4
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
