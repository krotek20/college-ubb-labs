% nrAparitii(nr,l1..ln):
%        0, n=0
%        1+nrAparitii(nr,l2..ln), l1=nr
%        nrAparitii(nr,l2..ln), altfel
%
% nrAparitii(E:element,L:list,R:Integer)
% Model de flux: (i,i,o) - determinist
% E: elementul caruia i se calculeaza numarul de aparitii in lista
% L: lista de elemente
% R: numarul de aparitii ale elementului E in lista L

nrAparitii(_,[],0).
nrAparitii(E,[E|T],R):-
    nrAparitii(E,T,R1),
    R is R1 + 1.
nrAparitii(E,[H|T],R):-
    E\=H,
    nrAparitii(E,T,R).


% elimina(l1..ln,c1..cm):
%        [], n=0
%        l1 + elimina(l2..ln), daca nrAparitii(L1,C) > 1
%        elimina(l2..ln,C), altfel
%
% elimina(L:list,C:list,R:list)
% Model de flux: (i,i,o) - determinist
% L: lista principala de elemente
% C: copie a listei initiale (lista curenta)
% R: lista rezultat
elimina([],_,[]).
elimina([H|T],C,R):-
    nrAparitii(H,C,1),
    !,
    elimina(T,C,R).
elimina([H|T],C,[H|R]):-
    elimina(T,C,R).


% eliminaPrincipal(l1..ln): elimina(l1..ln,l1..ln)
% eliminaPrincipal(L:list,R:list)
% Modelul de flux: (i,o) - determinist
% L: lista din care dorim sa eliminam
% R: lista rezultat
eliminaPrincipal(L,R):-
    elimina(L,L,R).
