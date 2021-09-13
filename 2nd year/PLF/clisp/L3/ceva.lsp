

(defun inlocuire (l e k)
	(cond
		((and (atom l) (eq e l)) k)
		((listp l) (mapcar #'(lambda (L) (inlocuire L e k) l))
		(t l)
	)
)