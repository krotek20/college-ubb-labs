% Dandu-se o lista liniara numerica, sa se stearga toate secventele de
% valori consecutive. Ex: sterg([1, 2, 4, 6, 7, 8, 10], L) va produce
% L=[4,10].
%
% Model matematic:
% sterg(l1..ln) = stergFara(l1, l2..ln)
% stergFara(E, l1..ln):
% - [E], daca n=0
% - E(+)stergFara(l1, l2..ln), daca E si l1 nu sunt consecutive
% - stergCu(E, l1..ln), altfel
% stergCu(E, l1..ln):
% - [], daca n=0
% - stergFara(l1, l2..ln), daca E si l1 nu sunt consecutive
% - stergCu(l1, l2..ln), altfel
%
% sterg(L:lista, R:lista)
% Model de flux: (i, o), (i, i) - determinist
% L: lista initiala
% R: lista rezultat
%
% stergFara(E:element, L:lista, R:lista)
% Model de flux: (i, i, o), (i, i, i) - determinist
% E: primul element al listei curente
% L: lista curenta
% R: lista rezultat
%
% stergCu(E:element, L:lista, R:lista)
% Model de flux: (i, i, o), (i, i, i) - determinist
% E: primul element al listei curente
% L: lista curenta
% R: lista rezultat

stergCu(_,[],[]).
stergCu(E, [H|T], R):-
    E =\= H-1,
    !,
    stergFara(H, T, R).
stergCu(_, [H|T], R):-
    stergCu(H, T, R).

stergFara(H,[],[H]).
stergFara(E, [H|T], R):-
    E =\= H-1,
    !,
    stergFara(H, T, R1),
    R=[E|R1].
stergFara(E, [H|T], R):-
    stergCu(E,[H|T], R).

sterg([H|T],R):- stergFara(H,T,R).
