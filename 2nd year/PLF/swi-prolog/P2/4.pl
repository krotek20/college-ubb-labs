% Se dau doua numere naturale n si m. Se cere sa se afiseze in toate modurile
% posibile toate numerele de la 1 la n, astfel incat intre orice doua
% numere afisate pe pozitii consecutive, diferenta in modul sa fie >=m.

% Model matematic:
% candidat(N):
% 1. N
% 2. candidat(N-1), daca N>1
% candidat(N:integer, I:integer)
% Model de flux: (i,o) - nedeterminist
% N: intreg care parcurge candidatii de la N la 1
% I: candidatul returnat
candidat(N,N).
candidat(N,I):-
    N>1,
    N1 is N-1,
    candidat(N1,I).

% Model matematic:
% apartine(l1..ln,I):
% - true, daca I apartine l1..ln
% - false, altfel
% apartine(L:lista, I:integer)
% Model de flux: (i,i) - determinist
% L: lista in care se cauta intregul I
apartine([H|_],H):- !.
apartine([_|T],I):- apartine(T,I).

% Model matematic:
% permutari_aux(N,M,S,l1..ln):
% 1. l , daca N=S
% 2. permutari_aux(N,M,S+1,I(+)(l1..ln), daca S<N si I=candidat(N)
%    si (l1-I >= M sau I-l1 >= M) si (I nu apartine l1..ln)
% permutari_aux(N:integer, M:integer, S:integer, Col:lista, L:lista)
% Model de flux: (i,i,i,i,o) - nedeterminist
% N: numarul de elemente din permutari
% M: intreg ce defineste conditia prin care doua elemente din permutare
%    trebuie sa fie aibe diferenta absoluta (in modul) mai mare sau
%    egala cu M
% S: lungimea curenta a listei colectoare
% Col: lista colectoare
% L: lista rezultat (o permutare rezultat)
permutari_aux(N,_,N,Col,Col):- !.
permutari_aux(N,M,S,[H|T],L):-
    candidat(N,I),
    abs(H-I)>=M,
    \+ apartine([H|T],I),
    S1 is S+1,
    permutari_aux(N,M,S1,[I|[H|T]],L).

% Model matematic:
% permutari(N,M)=permutari_aux(N,M,1,candidat(N))
% permutari(N:integer, M:integer, L:lista)
% Model de flux: (i,i,o) - nedeterminist
% N: numarul de elemente din permutari
% M: intreg pentru coditia din permutari
% L: lista rezultat (o permutare rezultat)
permutari(N,M,L):-
    candidat(N,I),
    permutari_aux(N,M,1,[I],L).

% Model matematic:
% toate(N,M)=*reuniune*(permutari(N,M))
% toate(N:integer, M:integer, L:lista)
% Model de flux: (i,o) - nedeterminist
toate(N,M,L):- findall(LRez,permutari(N,M,LRez),L).
