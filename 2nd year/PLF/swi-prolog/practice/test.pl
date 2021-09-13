g([H|_],E,[E,H]).
g([_|T],E,P):-
    g(T,E,P).
