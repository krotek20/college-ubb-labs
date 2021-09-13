; 9.b. Definiti o functie care inverseaza o lista impreuna cu toate sublistele
; sale de pe orice nivel.

; Model matematic
; invers_aux(L1..Ln, Col):
; Col, daca n = 0
; invers(L2..Ln, invers(L1, []) (+) Col), daca L1 este lista
; invers(L2..Ln, L1 (+) Col), altfel

(defun invers_aux (L Col)
	(cond
		((null L) Col)
		((listp (car L)) (invers_aux (cdr L) (cons
				(invers_aux (car L) ()) Col)))
		(t (invers_aux (cdr L) (cons (car L) Col)))
	)
)

; Model matematic
; invers(L1..Ln) = invers_aux(L1..Ln, [])
(defun invers (L)
	(invers_aux L ())
)