(declare-const x Bool)
(declare-const y Bool) 
(declare-const z Bool)
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)

(assert 
    (and
        (or z q x)
        (or (and x p) 
            (or (not q) x) 
            (and p y))
        (or 
            (and z y) 
            (and x (not r)))
        (or (not y) (not z) p)
        (or x 
            (and z p r) 
            (not y))
        (or 
            (and x p z) 
            (not r))
        (or y r)
    )
)

(check-sat)
(get-model)

(exit)