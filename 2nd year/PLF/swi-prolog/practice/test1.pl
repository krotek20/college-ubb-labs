candidat([H | _], H).
candidat([_ | T], C) :- candidat(T, C).

verif(X,N,X):- X =< N.
verif(X,N,R):- X =< N, X1 is X + 2, verif(X1, N, R).

numara([],0).
numara([_|T],N):- numara(T,N1), N is N1 + 1.

aranjamente(_, Col, 0, S, Col) :- mod(S,2) =:= 1.
aranjamente(L, Col, K, S, Rez) :-
    candidat(L, C),
    not(candidat(Col, C)),
    Col1 = [C | Col],
    K1 is K - 1,
    S1 is S + C,
    aranjamente(L, Col1, K1, S1, Rez).

aranjamenteWrapper(L, Rez) :-
    numara(L,N),
    verif(2,N,K),
    aranjamente(L, [], K, 0, Rez).

aranjamenteFindAll(L, Rez) :- findall(R, aranjamenteWrapper(L, R), Rez).


f([], -1).
f([H|T],S):- H>0, f(T,S1) ,S1<H, !, S is H.
f([_|T],S):- f(T,S1), S is S1.


% Creez un predicat auxiliar prin care elimin apelul dublu recursiv
% pe care il voi apela pe a doua ramura al primului predicat
% model de flux: (i,i,i,o) - determinist

f1([],-1).
f1([H|T],S):- f(T, S1), f_aux(H,T,S1,S).

f_aux(H,_,S1,S):- H > 0, S1 < H, !, S is H.
f_aux(_,_,S,S).
