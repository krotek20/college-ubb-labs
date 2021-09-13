% Se da o lista eterogena, formata din numere intregi si liste de
% numere intregi. Din fiecare sublista sa se stearga toate secventele de
% valori consecutive. De ex: [1, [2, 3, 5], 9, [1, 2, 4, 3, 4, 5, 7, 9],
% 11, [5, 8, 2], 7] => [1, [5], 9, [4, 7, 9], 11, [5, 8, 2], 7]
%
% Model matematic:
% stergPrincipal(l1..ln) = stergInSubliste(l1..ln)
% stergInSubliste(l1..ln):
% - [], daca n=0
% - sterg(l1_1..l1_m) (+) stergInSubliste(l2..ln),
%           daca l1 este lista
% - l1(+)stergInSubliste(l2..ln), altfel
%
% stergPrincipal(L:lista, R:lista)
% Model de flux: (i, o), (i, i) - determinist
% L: lista eterogena initiala
% R: lista eterogena rezultat
%
% stergInSubliste(L:lista, R:lista)
% Model de flux: (i, o), (i, i) - determminist
% L: lista eterogena curenta
% R: lista eterogena rezultat

stergInSubliste([], []).
stergInSubliste([H|T], R):-
    is_list(H),
    !,
    sterg(H, RH),
    stergInSubliste(T, R1),
    R = [RH|R1].
stergInSubliste([H|T], R):-
    stergInSubliste(T, R1),
    R = [H|R1].

stergPrincipal(L, R):- stergInSubliste(L, R).
