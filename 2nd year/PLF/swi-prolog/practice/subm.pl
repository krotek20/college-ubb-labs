subm([],[]).
subm([_|T],S):-subm(T,S).
subm([H|T],[H|S]):-subm(T,S).

toate(L,LRez):-findall(S,subm(L,S),LRez).
