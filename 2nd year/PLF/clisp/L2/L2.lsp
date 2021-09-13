; 7. Se da un arbore de tipul (1). Sa se precizeze nivelul pe care apare un nod
; x in arbore. Nivelul radacii se considera a fi 0. 

; Model matematic
; maxim(a,b):
; a, daca a > b
; b, altfel
; a, b - atomi numerici

(defun maxim (a b)
	(cond
		((> a b) a)
		(t b)
	)
)

; Model matematic
; find-level(tree, x, n):
; -1, daca am ajuns la frunza
; n, daca radacina este egala cu x
; maxim  ( find-level (subarb_stang x n+1),
;		 find-level (subarb_drept x n+1) ), altfel
;
; unde:
; tree este arbore de forma (radacina subarb_stang subarb_drept)
; x este elementul (nodul) cautat
; n este nivelul curent

(defun find-level (tree x n) 
	(cond 
		((null tree) -1)
		((equal (car tree) x) n)
		(t (maxim 
			(find-level (caddr tree) x (+ n 1))
			(find-level (cadr tree) x (+ n 1))
		))
	) 
)

; Model matematic
; find-wrapper(tree,x) = find-level(tree,x,0)

(defun find-wrapper (tree x)
	(find-level tree x 0)
)

; example: (find-wrapper '(a (b () (c)) (d (e (f)) (g))) 'e)
; example2: (A (B (D) (E (H))) (C (F (I)) (G)))