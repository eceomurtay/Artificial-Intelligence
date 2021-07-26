(declare-const a Bool) 
(declare-const b Bool) 
(declare-const c Bool) 
(declare-const d Bool) 
(declare-const e Bool) 
(declare-const f Bool) 

(assert 
    (and 
        (or 
            (and (not a) b d (or f (not c))) 
            (and a 
                (or d (not c) (or e a))
            )
        ) 
        (or f (and b (not e) (not f)))
        (or e f)
        (or b (and a c))
    )
)

(check-sat)
(get-model)

(exit)