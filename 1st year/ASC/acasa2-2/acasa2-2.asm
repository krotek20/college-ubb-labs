; maria are mere- cate vocale avem in fisier? "7" - rasp final de afisat pe ecran

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,fread,fopen,fclose,printf             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fopen msvcrt.dll 
import fread msvcrt.dll 
import printf msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    numefisier db 'sir.txt',0
    mod_acces db 'r',0
    descriptor dd -1
    
    numar dd 0
    len equ 100
    text times (len+1) db 0
    
    format db "Nr de vocale din fisier este: %d",0
    
; our code starts here
segment code use32 class=code
    start:
        push dword mod_acces
        push dword numefisier
        call [fopen]
        add esp, 4*2
        
        ; verificam daca s-a deschis fisierul
        cmp eax, 0
        je final
        
        mov [descriptor], eax
        
        ;citesc textul din fisier
        push dword [descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov esi, text
        
        repeta:
            lodsb
            
            cmp al, 0
            je final
            
            cmp    al, 'a'     
            je     vocala
            cmp    al, 'e'     
            je     vocala
            cmp    al, 'i'     
            je     vocala
            cmp    al, 'o'     
            je     vocala
            cmp    al, 'u'     
            je     vocala
            cmp    al, 'A'     
            je     vocala
            cmp    al, 'E'     
            je     vocala
            cmp    al, 'I'     
            je     vocala
            cmp    al, 'O'     
            je     vocala
            jmp    repeta
                
            vocala:
            inc    dword[numar] 
            jmp    repeta
            
        final:
            push dword [numar]
            push dword format
            call [printf]
            add esp, 4*2
            
            ;inchid fisierul
            push dword [descriptor]
            call [fclose]
            add esp, 4
        
        
        push    dword 0
        call    [exit]
