; 9.c. Dandu-se o lista, sa se construiasca lista primelor elemente ale tuturor
; elementelor lista ce au un numar impar de elemente la nivel superficial.
; Exemplu: (1 2 (3 (4 5) (6 7)) 8 (9 10 11)) => (1 3 9).

; Model matematic
; nr_elem(L1..Ln):
; 0, daca n=0
; nr_elem(L2..Ln) + 1, altfel
(defun nr_elem (L)
	(cond
		((null L) 0)
		(t (+ (nr_elem (cdr L)) 1)) 
	)
)

; Model matematic
; prim_elem_aux(L1..Ln, Col):
; Col, daca n=0
; prim_elem_aux(L2..Ln, Col (+) prim_elem_aux(L1, (L11))), 
;						daca L1 este lista si nr_elem(L1) % 2 = 1
;						(unde L11 L12 ... L1m = L1) 
; prim_elem_aux(L2..Ln, Col), altfel

(defun prim_elem_aux (L Col)
	(cond
		((null L) Col)
		((and (listp (car L)) (= (MOD (nr_elem (car L)) 2) 1))
			(prim_elem_aux (cdr L) (append
				Col (prim_elem_aux (car L) (list (caar L))))))
		(t (prim_elem_aux (cdr L) Col))
	)
)

; Model matematic
; prim_elem(L1..Ln) = prim_elem_aux([L], [])
(defun prim_elem (L)
	(prim_elem_aux (list L) ())
)