; 9.a. Sa se scrie o functie care intoarce diferenta a doua multimi.

; Model matematic
; apare(L1, K1..Km) =
; fals, daca m = 0
; t, daca L1 = K1
; apare(L1, K2..Km), altfel

(defun apare (L1 K)
	(cond
		((null K) nil)
		((equal L1 (car K)) t)
		(t (apare L1 (cdr K)))
	)
)

; Model matematic:
; diff(L1..Ln, K1..Km) = 
; [] , daca n = 0
; L1 (+) diff (L2..Ln, K1..Km), daca apare(L1, K1..Km) = NIL
; diff (L2..Ln, K1..Km), altfel

(defun diff (L K)
	(cond
		((null L) nil)
		((null (apare (car L) K)) (cons (car L) (diff (cdr L) K)))
		(t (diff (cdr L) K))
	)
)