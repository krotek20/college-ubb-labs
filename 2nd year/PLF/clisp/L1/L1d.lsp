; 9.d. Sa se construiasca o functie care intoarce suma atomilor numerici dintr-o
; lista, de la nivelul superficial.

; Model matematic
; suma(L1..Ln):
; 0, daca n=0
; L1 + suma(L2..Ln), daca L1 este atom numeric
; suma(L2..Ln), altfel

(defun suma (L)
	(cond
		((null L) 0)
		((numberp (car L)) (+ (car L) (suma (cdr L))))
		(t (suma (cdr L)))
	)
)