bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern fopen, fclose, fscanf, fprintf
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import fscanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    numfisier1 db 'fisier1.txt', 0
    numfisier2 db 'fisier2.txt', 0
    
    modacces1 db 'r', 0
    modacces2 db 'w', 0
    
    descriptor1 dd -1
    descriptor2 dd -1
    
    a dd 0
    b dd 0
    sumab dd 0
    sumcifre dd 0
    
    formatz db '%d', 0
    formath db '%x', 0
    formatlinienoua db 10, 0
    
    copie dd 0
    

; our code starts here
segment code use32 class=code
    start:
        ; deschidere fisier1
        push dword modacces1
        push dword numfisier1
        call [fopen]
        add esp, 4*2
        
        ; verificam daca s-a deschis fisierul
        cmp eax, 0
        je final
        
        mov [descriptor1], eax
        
        ; citire a
        push dword a
        push dword formatz
        push dword [descriptor1]
        call [fscanf]
        add esp, 4*3
        
        ; citire b
        push dword b
        push dword formatz
        push dword [descriptor1]
        call [fscanf]
        add esp, 4*3
        
        
        ; suma dintre a si b
        mov eax, [a]
        add eax, [b]
        mov [sumab], eax
        
        ; deschidere fisier2
        push dword modacces2
        push dword numfisier2
        call [fopen]
        add esp, 4*2
        
        cmp eax, 0
        je final
        
        mov [descriptor2], eax
        
        mov eax, [sumab]
        calcule:
            mov edx, 0             ; convert fara semn
            mov ebx, 10
            div ebx                ; eax - cat , edx - rest
            mov [copie], eax
            add [sumcifre], edx
            
            ; afisare cifra
            push dword edx
            push dword formatz
            push dword [descriptor2]
            call [fprintf]
            add esp, 4*3
            
            ; afisare linie noua
            push dword formatlinienoua
            push dword [descriptor2]
            call [fprintf]
            add esp, 4*2
            
            mov eax, [copie]
            cmp eax, 0
            jne calcule
        
        ; afisare suma cifre in hexa pe ultima linie
        push dword [sumcifre]
        push dword formath
        push dword [descriptor2]
        call [fprintf]
        add esp, 4*3
        
        ; inchidere fisier2
        push dword [descriptor2]
        call [fclose]
        add esp, 4*1
        
        ; inchidere fisier1
        push dword [descriptor1]
        call [fclose]
        add esp, 4*1
        
        final:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
