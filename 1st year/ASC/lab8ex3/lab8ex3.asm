; 26. Se da un sir de dublucuvinte. Sa se obtina sirul format din octetii superiori ai cuvintelor inferioare din elementele sirului de dublucuvinte, care sunt multiplii de 10.
; Exemplu:
; se da: s DD 12345678h, 1A2B3C4Dh, FE98DC76h
; rezultat: d DB 3Ch, DCh.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 12345678h, 1A2B3C4Dh, 0FE98DC76h
    ls equ ($-s)/4                  ; lungimea sirului s
    d times ls db 0                 ; declarare sir d
    zece db 10                      ; variabila folosita pentru testarea divizibilitatii cu 10
    aux db 0                        ; variabila auxiliara pentru pastrarea valorii curente din al (octetul superior al cuvantului inferior)
    
; our code starts here
segment code use32 class=code
    start:
        mov esi, s                  ; esi = offset s
        mov edi, d                  ; edi = offset d
        cld                         ; set DF = 0 (incrementare)
        mov ecx, ls                 ; pentru loop (se repeta de ls ori)
        repeta:
            lodsw                   ; in ax vom avea cuvantul mai putin semnificativ al dublucuvantului curent din sir
            shr ax, 8               ; pastram doar octetul superior din acesta
            mov byte[aux], al       ; il pastram in aux
            div byte[zece]          ; al = cat, ah = rest
            cmp ah, 0               ; comparam restul cu 0
            je adauga               ; daca restul este 0 atunci valoarea testata este multiplu de 10
            jmp nonmultiplu         ; altfel nu este
            adauga:
                mov al, byte[aux]   ; recuperam valoarea octetului superior din cuvantul inferior din dublucuvantul curent
                stosb               ; o adaugam in sirul d (sir rezultat)
            nonmultiplu:
                lodsw               ; in final, parcurgem fictiv cuvantul superior pentru a putea ajunge la urmatorul cuvant inferior
        loop repeta
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
