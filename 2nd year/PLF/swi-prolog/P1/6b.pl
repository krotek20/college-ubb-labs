% Sa se elimine toate aparitiile elementului maxim dintr-o lista de numere
% intregi.

% remMax_aux(L:list,M:element,R:list)
% (i,i,o),(i,i,i) - determinist

% remMax_aux(L,M,R):
%      multimea vida, daca L este vida
%      remMax_aux(T,M,R1), daca H\=M
%      remMax_aux(T,M,R), altfel

remMax_aux([], _, []).

remMax_aux([H|T], M, R):-
	H \= M, !,
	remMax_aux(T, M, R1),
	R = [H|R1].

remMax_aux([_|T], M, R):-
	remMax_aux(T, M, R).

% remMax(L:list,R:list)
% (i,o),(i,i) - determinist

remMax(L, R):-
	max(L, M),
	remMax_aux(L, M, R).
