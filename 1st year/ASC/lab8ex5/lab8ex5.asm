; Sortarea unui sir de dublucuvinte (descrescator)
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 12345678h, 1A2B3C4Dh, 0FE98DC76h, 56127A8Bh, 0FFEE8877h
    ls equ ($-s)/4-1                    ; lungimea sirului s -1 pentru compararea contorului cu capatul de sir
    aux dd 0                            ; variabila auxiliara pentru interschimbare
    i dd 0                              ; \ contoare pentru incarcarea
    j dd 0                              ; / dublucuvintelor din sir
    i2 db 0                             ; \\ contoare pentru parcurgerea
    j2 db 0                             ; // in lungime a sirului

; our code starts here
segment code use32 class=code
    start:
        mov ecx, 4                      ; cu ecx vom creste contoarele i si j
        cld                             ; DF = 0 (incrementare)
        repeta:
            mov esi, s                  ; esi = offset s
            add esi, dword[i]           ; esi = offset s1 + i (contor pentru elementul curent din s)
            lodsd                       ; eax <- esi[i] (dublucuvantul de la adresa ds:esi + i) , esi += 4
            mov ebx, eax                ; ebx = eax
            
            mov edx, dword[i]           ; \ j va primii 
            mov dword[j], edx           ; / valoarea lui i (pentru parcurgerea de la i+1)
            
            mov al, byte[i2]            ; \ j2 va primii
            mov byte[j2], al            ; / valoarea lui i2 (pentru cresterea contorului pana la ls)
            comparare:
                add dword[j], ecx       ; j += 4
                inc byte[j2]            ; j2 += 1
                mov esi, s              ; esi = offset s
                add esi, dword[j]       ; esi = offset s2 + j (contor pentru elementul curent din s)
                lodsd                   ; eax <- esi[j] (dublucuvantul de la adresa ds:esi + j) , esi += 4
                cmp ebx, eax            ; comapram cele doua elemente
                jb interschimb          ; daca primul e mai mic se face interschimbarea
                
                cmp byte[j2], ls        
                je final                ; daca am ajuns la capatul sirului sarim la final
                jmp comparare           ; altfel repetam
            interschimb:
                mov edi, dword[i]       ; elementul de pe pozitia i
                mov ebp, dword[j]       ; elementul de pe pozitia j
                                        ; interschimbarea a doua elemente din sirul s 
                mov edx, [s+edi]
                mov dword[aux], edx
                mov edx, [s+ebp]
                mov [s+edi], edx
                mov edx, dword[aux]
                mov [s+ebp], edx
                
                mov ebx, [s+edi]        ; in ebx pastram elementul de pe pozitia i
                
                cmp byte[j2], ls        
                je final                ; daca am ajuns la capatul sirului sarim la final
                jmp comparare           ; altfel repetam
            final:
                add dword[i], ecx       ; i += 4
                inc byte[i2]            ; i2 += 1
                cmp byte[i2], ls
                je final2               ; daca am ajuns la capatul sirului am terminat problema
                jmp repeta              ; altfel repetam
        final2:
                
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
