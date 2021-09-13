; 10. Definiti o functie care determina numarul nodurilor de pe nivelul k
; dintr-un arbore n-ar reprezentat sub forma (radacina lista_noduri_subarb1
; ... lista_noduri_subarbn) Ex: arborelele este (a (b (c)) (d) (e (f))) si
; k=1 => 3 noduri 

; Model matematic
; find-count(x, k, n):
; 1, daca k = n si x este atom
; ∑i=1,m (find-count(xi, k, n+1)), unde x=(x1 x2 ... xm)
; 0, altfel
;
; unde: k = nivelul de input, n = nivelul curent

(defun find-count (x k n)
	(cond
		((and (= k n) (atom x)) 1)
		((listp x) (apply '+ (mapcar #'
			(lambda (l) 
				(find-count l k (+ 1 n))) 
			x))
		)
		(t 0)
	)
)

; Model matematic
; find-k-nodes(tree,k) = find-count(tree,k,-1)

(defun find-k-nodes (tree k)
	(find-count tree k -1)
)

; example: (find-k-nodes '(1 (2 a (b) (c)) (d) (5 (6 (7) e))) 2) = 4