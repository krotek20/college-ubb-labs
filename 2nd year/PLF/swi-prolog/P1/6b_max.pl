% max(L:list,R:element)
% (i,o) - determinist

% max(L,R):
%     -99999, daca L este vida
%     max(T,R1), daca H > R1
%     max(T,R1), altfel

max([], -99999).

max([H|T], R):-
	max(T, R1), H > R1,
	R is H, !.

max([_|T], R):-
	max(T, R).
