% Sa se scrie un predicat care elimina dintr-o lista toate elementele care
% se repeta (ex: l=[1,2,1,4,1,3,4] => l=[2,3])

% remPlurals_aux(L1:list,L2:list,R:list)
% (i,i,o),(i,i,i) - determinist

% remPlurals_aux(l1..ln,r1..rn):
%     multimea vida, daca L1 este vida
%     l1 + remPlurals_aux(l2,..,ln,L), daca count(L1,R) > 1
%     remPlurals_aux(l2,..,ln,L), altfel
remPlurals_aux([], _, []).

remPlurals_aux([H|T], L, R):-
	count(L, H, O), O == 1,
	remPlurals_aux(T, L, R1),
	R = [H|R1], !.

remPlurals_aux([_|T], L, R):-
	remPlurals_aux(T, L, R).

%remPlurals(L:list,R:list)
%(i,o),(i,i) - determinist

remPlurals(L, R):-
	remPlurals_aux(L, L, R).
