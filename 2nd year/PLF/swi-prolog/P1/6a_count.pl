% count(L:list,E:element,R:integer)
% (i,i,o) - determinist
% count(l1l2...ln,E):
%     0, daca L e vida
%     1+count(l2l3...ln,E,R), E == l1
%     count(l2l3...ln,E,R), altfel
count([], _, 0).

count([H|T], E, R):-
	count(T, E, R1), E == H,
	R is R1 + 1, !.

count([_|T], E, R):-
	count(T, E, R).
