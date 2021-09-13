bits 32

global start        

extern exit, printf        
import exit msvcrt.dll    
import printf msvcrt.dll
segment data use32 class=data

    ;a string of dwords is given. From each of these dwords form a new word by taking the higher byte of the higher word and the higher byte of the lower word
    ;all these words will be stored in a word string. Then compute the number of bits of value 1 from the new formed word string and print it on the screen in base 10.
    ;explain the algorithm, justify and comment the source code

    dwordString dd 12345678h, 11223344h, 1A2B3C4Dh
    len equ ($-dwordString)/4
    wordString resw len
    
    nrBiti resd 1
    formatNr db '%d', 0
segment code use32 class=code
    start:
        
        
        mov ecx, 0
        .repeta:
            
            mov al, [dwordString + ecx*4 + 1]
            mov ah, [dwordString + ecx*4 + 3]
            mov [wordString + ecx*2], ax

            inc ecx
            cmp ecx, len
            jb .repeta
            
        mov ecx, len
        mov esi, wordString
        cld
        .repetaNrBiti:
            lodsw
            mov bx, 1
            .repeta2:
                test ax, bx
                jz .over
                inc dword[nrBiti]
                .over:
                shl bx, 1
                cmp bx, ax
                jbe .repeta2
            loop .repetaNrBiti
            
        push dword[nrBiti]
        push formatNr
        call [printf]
        
        ; exit(0)
        push    dword 0
        call    [exit]