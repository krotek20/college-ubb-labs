; Model matematic:
; inlocuieste(X, E, K) = 
; K, daca X == E
; X, daca X != E si X este atom
; (inlocuieste(X1, E, K), inlocuieste(X2, E, K), ..., inlocuieste(Xn, E, K)), 
;		daca X este lista, unde X1, ..., Xn = X

; X - Lista de elemente
; E - Elementul cautat
; K - Elementul cu care se inlocuieste E

(defun inlocuieste (x e k)
	(cond 
		((equal x e) k)
		((atom x) x)
		(t (mapcar #'(lambda (l)
					(inlocuieste l e k)
		) x))
	)
)