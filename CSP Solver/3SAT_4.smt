(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)
(declare-const w Bool)

(assert
    (and 
        (or z 
            (and w
                (or (not x) y) 
                (not y))) 
        (or x 
            (not (or y z)))
        (or (not x) 
            (and y x (not z)))
        (or z w
            (or (not x) y))
        (or w y 
            (not x) 
            (and w z))
    )
)

(check-sat)
(get-model)

(exit)