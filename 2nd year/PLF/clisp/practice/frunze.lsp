; V1

(defun afisareFaraMapFrunze(l)
	(cond
		((eq (cadr l) nil) (list (car l)))
		((eq (caddr l) nil) (afisareFaraMapFrunze (cadr l)))
		((eq (cadddr l) nil) (append (afisareFaraMapFrunze (cadr l))) (afisareFaraMapFrunze (caddr l)))
	)
)

(defun afisareFrunze(l)
	(cond
		((null (cdr l)) l)
		(t (apply #'append (mapcar #'afisareFrunze (cdr l))))
	)
)

(defun afisareFrunzeMapCan(l)
	(cond
		((null (cdr l)) l)
		(t (mapcan #'afisareFrunze (cdr l)))
	)
)

; V2

; afisareFrunze(L1, ..., Ln) = ((L1), L3, ..., Ln), L2 == 0
;							   afisareFrunze(L3, ..., Ln), L2 == 1
;							   (v11 U v21, v22), L2 == 2 (altfel), v11, v12 = afisareFrunze(L3, ..., Ln), v21, v22 = afisareFrunze(v11)

(defun afisareV2Frunze(l)
	(cond
		((= (cadr l) 0) (list (list (car l)) (cddr l)))
		((= (cadr l) 1) (afisareV2Frunze (cddr l)))
		(t  ((lambda(v22)
				((lambda(v12)
					(list (append (car v22) (car v12)) (cadr v12)))
				(afisareV2Frunze (cadr v22))))
			(afisareV2Frunze (cddr l)))
		)
	)
)

(defun f (X Y)
	(cond
		((numberp X) X)
		((atom X) Y)
	)
)


(defun lista_aux (l col)
 (cond
 ((null l) col)
 ((numberp (car l)) (lista_aux (cdr l) (append col (list (car l)))))
 (t (lista_aux (cdr l) col))
 )
)
(defun lista (l)
 (lista_aux l nil)
)