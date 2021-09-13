; 16. Se dau doua siruri de caractere ordonate alfabetic s1 si s2. Sa se construiasca prin interclasare sirul ordonat s3 care sa contina toate elementele din s1 si s2. (cu lods / stos / ...)
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 db 'A', 'E', 'K', 'L'
    l1 equ $-s1
    s2 db  'B', 'D', 'F', 'J', 'N', 'O', 'P'
    l2 equ $-s2
    s3 times l1+l2 db 0
    i dd 0                             ; contor sir s1
    j dd 0                             ; contor sir s2
    k dd 0                             ; contor sir s3

; our code starts here
segment code use32 class=code
    start:
        cld                            ; DF = 0 (incrementare contor sir)
        inceput_while:
            mov esi, s1                ; esi = offset s1
            add esi, dword[i]          ; esi = offset s1 + i (contor pentru elementul curent din s1)
            lodsb                      ; al = esi[i] (octetul de la adresa ds:esi + i) , esi += 1
            mov bl, al                 ; bl = al
            
            mov esi, s2                ; esi = offset s2
            add esi, dword[j]          ; esi = offset s2 + j (contor pentru elementul curent din s2)
            lodsb                      ; al = esi[j] (octetul de la adresa ds:esi + j) , esi += 1
            mov bh, al                 ; bh = al
            
            cmp bl, bh                 ; comparam cele doua elemente din s1 si s2
            jb adauga_s1               ; daca elementul din s1 este mai mic din punct de vedere lexicografic se va adauga in s3
            jmp adauga_s2              ; altfel elementul din s2 se va adauga in s3
            adauga_s2:
                mov al, bh             ; al = bh
                mov edi, s3            ; edi = offset s3
                add edi, dword[k]      ; edi = offset s3 + k (contor pentru elementul curent din s3)
                stosb                  ; edi[k] = al , edi += 1
                inc dword[k]           ; incrementam contorul lui s3
                inc dword[j]           ; incrementam contorul lui s2
                jmp final              ; salt conditionat dupa finalizarea adaugarii
            adauga_s1:
                mov al, bl             ; al = bl
                mov edi, s3            ; edi = offset s3
                add edi, dword[k]      ; edi = offset s3 + k (contor pentru elementul curent din s3)
                stosb                  ; edi[k] = al , edi += 1
                inc dword[k]           ; incrementam contorul lui s3
                inc dword[i]           ; incrementam contorul lui s1
            final:
                cmp dword[i], l1       ; comparam pozitia curenta in sirul s1 cu lungimea acestuia
                je s2_while            ; daca sunt egale inseamna ca am adaugat toate elementele sirului s1 in s3 asa ca vom adauga elementele ramase din s2
                cmp dword[j], l2       ; comparam pozitia curenta in sirul s2 cu lungimea acestuia
                je s1_while            ; daca sunt egale inseamna ca am adaugat toate elementele sirului s2 in s3 asa ca vom adauga elementele ramase din s1
                jmp inceput_while      ; altfel se reia while-ul
        s2_while:
            mov esi, s2                ; esi = offset s2
            add esi, dword[j]          ; esi = offset s2 + j (contor pentru elementul curent din s2)
            movsb                      ; lodsb + stosb => la adresa lui es:esi se incarca octetul de la adresa ds:esi
            inc dword[j]               ; incrementam contorul lui s2
            cmp dword[j], l2           ; comparam pozitia curenta in sirul s2 cu lungimea acestuia
            je final2                  ; daca sunt egale obtinem sirul final s3
            jmp s2_while               ; altfel adaugam mai departe elemente din s2 in s3
        s1_while:
            mov esi, s1                ; esi = offset s1
            add esi, dword[i]          ; esi = offset s1 + i (contor pentru elementul curent din s1)
            movsb                      ; lodsb + stosb => la adresa lui es:esi se incarca octetul de la adresa ds:esi
            inc dword[i]               ; incrementam contorul lui s1
            cmp dword[i], l1           ; comparam pozitia curenta in sirul s1 cu lungimea acestuia
            je final2                  ; daca sunt egale obtinem sirul final s3
            jmp s1_while               ; altfel adaugam mai departe elemente din s1 in s3
        final2:
            
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
